import { createShareCard, type ShareCardData } from '../lib/share-card';

const root = document.querySelector<HTMLElement>('#concept-share');
if (root) {
  const data: ShareCardData = JSON.parse(root.dataset.card!);
  const filename = root.dataset.filename!;
  const preview = root.querySelector<HTMLElement>('#share-preview')!;
  const image = root.querySelector<HTMLImageElement>('#share-image')!;
  const fallback = root.querySelector<HTMLElement>('#share-fallback')!;
  const copy = root.querySelector<HTMLButtonElement>('#copy-share-image')!;
  const save = root.querySelector<HTMLAnchorElement>('#save-share-image')!;
  const share = root.querySelector<HTMLButtonElement>('#native-share-image')!;
  const retry = root.querySelector<HTMLButtonElement>('#retry-share-image')!;
  const message = root.querySelector<HTMLElement>('#share-message')!;
  let blob: Blob | undefined;
  let file: File | undefined;
  const canCopy = window.isSecureContext && typeof ClipboardItem !== 'undefined' && typeof navigator.clipboard?.write === 'function';

  async function generate() {
    retry.hidden = true;
    preview.setAttribute('aria-busy', 'true');
    message.textContent = '正在生成分享图片…';
    try {
      const card = await createShareCard(data);
      blob = card.blob;
      image.src = card.src;
      await image.decode();
      image.hidden = false;
      fallback.hidden = true;
      save.href = card.src;
      save.hidden = false;
      copy.disabled = false;
      copy.textContent = canCopy ? '复制图片' : '长按或保存图片';
      file = new File([blob], filename, { type: 'image/png' });
      try { share.hidden = !(navigator.canShare?.({ files: [file] }) && navigator.share); }
      catch { share.hidden = true; }
      message.textContent = canCopy ? '图片已就绪，可以复制或保存。' : '当前浏览器不支持直接复制图片，请长按图片或点击「保存图片」。';
    } catch (error) {
      message.textContent = '图片生成失败，请重试。也可先扫描二维码阅读全文。';
      retry.hidden = false;
      console.error('Share image generation failed', error);
    } finally {
      preview.setAttribute('aria-busy', 'false');
    }
  }

  copy.addEventListener('click', async () => {
    if (!blob) return;
    if (!canCopy) {
      image.scrollIntoView({ behavior: 'smooth', block: 'center' });
      message.textContent = '请长按下方图片保存，或点击「保存图片」后发到微信。';
      return;
    }
    try {
      // The PNG is prepared before the click to preserve Safari's user activation.
      await navigator.clipboard.write([new ClipboardItem({ 'image/png': blob })]);
      message.textContent = '图片已复制。打开微信聊天，粘贴即可发送。';
    } catch {
      message.textContent = '未能复制图片。请点击「保存图片」，或在手机上长按图片保存。';
    }
  });
  share.addEventListener('click', async () => {
    if (!file) return;
    try { await navigator.share({ files: [file], title: data.title }); }
    catch (error) {
      if (!(error instanceof DOMException && error.name === 'AbortError')) {
        message.textContent = '未能打开分享菜单，请保存图片后发到微信。';
      }
    }
  });
  save.addEventListener('click', () => {
    message.textContent = '如手机没有自动保存，请长按图片选择保存。';
  });
  retry.addEventListener('click', () => { void generate(); });
  void generate();
}
