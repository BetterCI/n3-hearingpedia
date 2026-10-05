import type { Reference } from './references';

export const dynamicRangeReferences: Record<string, Reference> = {
  "moore-softness-2004": {
    "title": "Testing the concept of softness imperception: Loudness near threshold for hearing-impaired ears",
    "authors": "Moore, B. C. J.",
    "year": "2004",
    "publication": "The Journal of the Acoustical Society of America, 115(6), 3103–3111",
    "doi": "10.1121/1.1738839",
    "url": "https://pubmed.ncbi.nlm.nih.gov/15237835/",
    "access": "abstract",
    "supports": "核对原论文摘要与Crossref摘要：接近听阈的响度匹配结果，不将重振概括为阈值以上立即出现很响的感觉。"
  },
  "wiggins-seeber-2011": {
    "title": "Dynamic-range compression affects the lateral position of sounds",
    "authors": "Wiggins, I. M. & Seeber, B. U.",
    "year": "2011",
    "publication": "The Journal of the Acoustical Society of America, 130(6), 3939–3953",
    "doi": "10.1121/1.3652887",
    "url": "https://portal.fis.tum.de/en/publications/dynamic-range-compression-affects-the-lateral-position-of-sounds/",
    "access": "abstract",
    "supports": "核对作者机构摘要与Crossref摘要：正常听力者、虚拟声学刺激和独立快速压缩的左右位置知觉，不直接推广所有实际双侧设备。"
  },
  "croghan-music-2014": {
    "title": "Music preferences with hearing aids: effects of signal properties, compression settings, and listener characteristics",
    "authors": "Croghan, N. B. H., Arehart, K. H. & Kates, J. M.",
    "year": "2014",
    "publication": "Ear and Hearing, 35(5), e170–e184",
    "doi": "10.1097/AUD.0000000000000056",
    "url": "https://pubmed.ncbi.nlm.nih.gov/25010635/",
    "access": "abstract",
    "supports": "核对原论文摘要：18名有助听器经验的听者、模拟助听器、古典和摇滚音乐偏好。区分快速压缩的偏好结果与言语识别结果。"
  },
  "zeng-compression-2004": {
    "title": "Compression and Cochlear Implants",
    "authors": "Zeng, F.-G.",
    "year": "2004",
    "publication": "In S. P. Bacon, R. R. Fay & A. N. Popper (Eds.), Compression: From Cochlea to Cochlear Implants, pp. 184–220. Springer",
    "url": "https://bpb-us-e2.wpmucdn.com/faculty.sites.uci.edu/dist/6/480/files/2021/09/2004-Zeng-Compression-Bacon-Book.pdf",
    "access": "fulltext",
    "supports": "核对公开章节第5.2节及公式5.2.1—5.2.3，用于图2对数幅度映射与分贝坐标转换；基础模型，不代表现代设备完整算法或统一参数。"
  }
};
