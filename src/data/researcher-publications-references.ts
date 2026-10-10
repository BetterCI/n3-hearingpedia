import type { Reference } from './references';

// Publication metadata and access scope checked on 2026-10-10.
export const researcherPublicationReferences: Record<string, Reference> = {
  'jeffress-hixon-book-1951': {
    title: 'Cerebral Mechanisms in Behavior: The Hixon Symposium', authors: 'Lloyd A. Jeffress（编）', year: '1951',
    publication: 'John Wiley & Sons, New York；xiv + 311页', url: 'https://calteches.library.caltech.edu/1314/1/books.pdf', access: 'metadata',
    supports: 'Caltech同期书评明确题名、Jeffress编辑身份、出版社及1948年会议背景；1951年出版时间另由图书馆数字书目互证。未取得文集全文，不把各篇论文归为编辑独著。',
  },
  'house-memoir-2011': {
    title: 'The Struggles of a Medical Innovator: Cochlear Implants and Other Ear Surgeries', authors: 'William F. House', year: '2011',
    publication: 'CreateSpace；个人回忆录', url: 'https://www.audiologyonline.com/interviews/interview-with-william-house-m-1337', access: 'metadata',
    supports: '2011年8月29日作者访谈核对新回忆录的完整题名、出版渠道和内容范围。未读取全书；回忆录不替代临床效果研究，也不将访谈提及的House Clinic其他作者著作归为William House个人著作。',
  },
  'helmholtz-vowels-1859': {
    title: 'Ueber die Klangfarbe der Vocale', authors: 'H. Helmholtz', year: '1859',
    publication: 'Annalen der Physik, 184(10): 280–290', doi: '10.1002/andp.18591841004', url: 'https://onlinelibrary.wiley.com/doi/10.1002/andp.18591841004', access: 'metadata',
    supports: '出版社书目核对题名、作者、1859年和页码，仅登记元音音色研究的原始论文入口；具体音叉合成论述另据已核验《音的感觉》相关章节，不据题名补写本论文实验结果。',
  },
  'schroeder-fractals-book-1991': {
    title: 'Fractals, Chaos, Power Laws: Minutes from an Infinite Paradise', authors: 'Manfred Schroeder', year: '1991',
    publication: 'W. H. Freeman；ISBN 0-7167-2136-8', url: 'https://www.cambridge.org/core/journals/mathematical-gazette/article/abs/fractals-chaos-power-laws-minutes-from-an-infinite-paradise-by-manfred-schroeder-pp-429-2449-1991-isbn-0716721368-freeman/D9280A19DD2DF4126D71473F8A2FBCAF', access: 'metadata',
    supports: '出版社保存的书评题名核对作者、完整书名、1991年与Freeman版本。未取得全书，不以书评页面的数字化日期代替书籍出版年，不把跨学科著作当作新的听觉实验。',
  },
  'chao-collected-papers-2002': {
    title: '赵元任语言学论文集', authors: '赵元任 著；吴宗济主编；赵新那等整理', year: '2002',
    publication: '商务印书馆；出版社当前记录ISBN 978-7-100-03127-1', url: 'https://www.cp.com.cn/book/7-100-03127-3_93.html', access: 'metadata',
    supports: '读取出版社书目、吴宗济序、赵新那后记和目录；核对2002年出版、2024年印刷与著述/编选分工。未取得全书，不把当前简介所述英文卷篇数当作全部论文数量。',
  },
  'chao-language-problems-book': {
    title: '语言问题', authors: '赵元任', year: '1980（所核版本）',
    publication: '商务印书馆；ISBN 978-7-100-02641-3', url: 'https://www.cp.com.cn/Plus/ContentKeywords/?ID=2221', access: 'metadata',
    supports: '出版社书目与内容介绍核对所列1980年6月版本、演讲记录及16讲范围；不是断言初版为1980年。未取得全书，不补写具体实验结论。',
  },
  'chao-tone-letters-1930': {
    title: 'A system of tone-letters', authors: 'Yuen Ren Chao', year: '1930',
    publication: 'Le Maître Phonétique, troisième série, no. 30: 24–27', url: 'https://www.wiedenhof.nl/ul/cnow21ss.htm', access: 'metadata',
    supports: '作者学术课程页面列出的原始文献与扫描入口核对题名、1930年及24–27页；五度相对轮廓的介绍另与已核验1933年论文第126页及脚注互证。未声称通读1930年原文。',
  },
  'wu-spectrographic-atlas-1986': {
    title: '汉语普通话单音节语图册', authors: '吴宗济（主编）', year: '1986',
    publication: '中国社会科学出版社，北京；NCID BN05516560', url: 'https://ksucat2.kyoto-su.ac.jp/webopac/catdbl.do?hidden_return_link=true&pkey=BB00900739', access: 'metadata',
    supports: '京都产业大学图书馆原始馆藏书目核对主编、1986年9月、出版社、英文题名与语图册属性；未取得全书，不从书目推断具体发音人、测量参数或统计结果。',
  },
  'wu-experimental-phonetics-book': {
    title: '实验语音学概要', authors: '吴宗济、林茂灿（主编）', year: '1989（所列版本）',
    publication: '高等教育出版社，北京', url: 'https://mirrors.sustech.edu.cn/courses/syllabus/HUM046.pdf', access: 'metadata',
    supports: '大学课程书目直接列出吴宗济、林茂灿主编、1989年及高等教育出版社，与商务印书馆论文集序言的合编记录互证。未取得全书；不混同其他作者后来的增订版。',
  },
  'ma-acoustics-handbook-2004': {
    title: '声学手册（修订版）', authors: '马大猷、沈㠙 著', year: '2004（修订第二版）',
    publication: '科学出版社；ISBN 7-03-012545-2；初版1983', url: 'https://www.ecsponline.com/yz/B823288121DD3415CA3CA2CAECD7A2936000.pdf', access: 'metadata',
    supports: '下载并逐页查看出版社试读扉页与版权页，核对两位作者（扉页姓名为沈㠙，文本层CIP异字不据以改名）、1983年初版、2004年7月修订第二版、出版社与ISBN。书目另与声学所专著目录互证；未取得整书。',
  },
  'ma-mpp-theory-1975': {
    title: '微穿孔板吸声结构的理论和设计', authors: '马大猷', year: '1975',
    publication: '中国科学，第1期: 38–50', url: 'https://www.sciengine.com/doi/pdf/f34434018b9141ea878d67eded26afe2', access: 'abstract',
    supports: '原论文可检索摘要与开篇核对微孔自身提供声阻、取消额外多孔材料及设计图表的研究范围；年份与中科院2024年机构报道互证，页码与后续论文文献表互证。未通读或重算全部原文，不引用摘要的普遍效果措辞。',
  },
  'ma-mpp-wideband-1987': {
    title: 'Microperforated-Panel Wideband Absorbers', authors: 'Dah-You Maa', year: '1987',
    publication: 'Noise Control Engineering Journal, 29(3): 77–84', doi: '10.3397/1.2827694', url: 'https://doi.org/10.3397/1.2827694', access: 'metadata',
    supports: '出版社提交Crossref的元数据核对题名、作者、1987年、29卷3期与起始页77；末页84由后续原始研究参考文献互证。仅作宽带微穿孔吸声研究的书目入口，未取得全文。',
  },
  'ma-mpp-potential-1998': {
    title: 'Potential of microperforated panel absorber', authors: 'Dah-You Maa', year: '1998',
    publication: 'The Journal of the Acoustical Society of America, 104(5): 2861–2866', doi: '10.1121/1.423870', url: 'https://doi.org/10.1121/1.423870', access: 'abstract',
    supports: '出版社提交Crossref的摘要及书目核对结构参数与吸声特性之间的设计关系；OpenAlex仅用于发现与引用链定位。未取得全文，不把摘要中的频带范围写成任意实际房间均可取得的结果。',
  },
};
