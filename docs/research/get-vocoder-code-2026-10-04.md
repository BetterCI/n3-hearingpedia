# GET 声码器代码入口核验

核验日期：2026-10-04。仓库：[BetterCI/GETVocoder](https://github.com/BetterCI/GETVocoder)。原始 GET 论文正文提供此仓库链接；本次读取仓库 README、GETvoc.m、VocMain.m、VocMain_Batch.m，并通过 GitHub API 核对文件树。

- 默认分支：main；核验提交：`7f9e65435a07477b22df08fefdc3046428ad7065`；最后推送：2023-02-17。
- README 指定 MATLAB R2020a 或更新版本，演示入口为 VocMain.m；GETvoc.m 为核心合成函数。
- VocMain.m 默认 vocoderCarrier=1（GET）；VocMain_Batch.m 默认为 2（GEN）。批处理脚本读取 WAV 并保存输出，词条明确提醒载波选择。
- ACEStrategy.m 和 ACE/ 为刺激图研究处理链；README 说明 ACE 部分改编自 CCi-MOBILE。
- 文件树未检出独立许可文件，GitHub API license 字段为空；README 将用途限定为学术研究，不据此宣称通用开源许可或商业使用权。
- 本次只核对文档与代码，未安装、运行或验证 MATLAB 运行环境，不声称其与临床处理器等价。

词条加入独立代码小节、四项文件入口及编号来源 get-vocoder-code；参考来源总数更新为 121，逐词条证据映射随构建更新。
