# Estate

项目当前文档见: [文档](https://tower.im/projects/860a30505cfe40deaec4905e48358201/docs/ae4b090f499d44579fa9c960c17a72c2/)

*以下为历史文档*

-----

## 网页抓取

### 数据条目结构

```
CREATE TABLE `estate` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `url` varchar(200) NOT NULL DEFAULT '',
  `website` varchar(16) DEFAULT NULL,
  `location` varchar(16) DEFAULT NULL,
  `published_at` datetime DEFAULT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `html` mediumtext,
  `content` mediumtext,
  `seg_freq` mediumtext,
  `topic` bigint(20) DEFAULT NULL,
  `status` int(10) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `url_index` (`url`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

Q1
```
CREATE TABLE `estate_q1` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `url` varchar(200) NOT NULL DEFAULT '',
  `website` varchar(16) DEFAULT NULL,
  `location` varchar(16) DEFAULT NULL,
  `published_at` datetime DEFAULT NULL,
  `created_at` TIMESTAMP NOT NULL,
  `html` mediumtext,
  `content` mediumtext,
  `seg_freq` mediumtext,
  `topic` bigint(20) DEFAULT NULL,
  `status` int(10) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `url_index` (`url`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

Q2
```
CREATE TABLE `estate_q2` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `url` varchar(200) NOT NULL DEFAULT '',
  `website` varchar(16) DEFAULT NULL,
  `location` varchar(16) DEFAULT NULL,
  `published_at` datetime DEFAULT NULL,
  `created_at` TIMESTAMP NOT NULL,
  `html` mediumtext,
  `content` mediumtext,
  `seg_freq` mediumtext,
  `topic` bigint(20) DEFAULT NULL,
  `status` int(10) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `url_index` (`url`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

```
INSERT INTO estate_q2 (url, website, location, published_at, html)
SELECT url, website, location, published_at, html
FROM estate WHERE published_at >= '2015-04-01' and published_at < '2015-07-01';
```


### 目标网站（以及对应的城市location）

```
搜房房地产   http://www.fang.com/news/
新浪乐居    http://www.house.sina.com.cn/
搜狐焦点    http://www.focus.cn/
网易房产    http://house.163.com/
中国房地产信息网    http://www.realestate.cei.gov.cn/
中国房地产网  http://www.china-crb.cn/
人民网房产   http://house.people.com.cn/
腾讯房产    http://house.qq.com/
凤凰房产    http://house.ifeng.com/
365房产网  http://news.house365.com/
中房网 http://www.fangchan.com/
地产中国网   http://house.china.com.cn/
央视经济房产  http://jingji.cntv.cn/house/20131016.shtml
和讯房产    http://house.hexun.com/
新华房产网   http://www.xinhuanet.com/house/
21世纪中国不动产   http://www.century21cn.com/
首都热线    http://www.shoudurx.com/
天津北方网   http://www.enorth.com.cn/
上海热线房地产 http://www.online.sh.cn/
上海网 http://www.sh021.cc/
华龙网 http://www.cqnews.net/
河北网 http://www.he-bei.cn/
商都网 http://www.shangdu.com/
云南101网  http://www.yn101.com/
东北新闻网   http://www.nen.com.cn/
今日黑龙江网  http://www.jrhlj.com/
湖南在线    http://hunan.voc.com.cn/
安徽门户网   http://www.ahoah.com/
山东信息港   http://www.ingsd.com/
亚心网 http://www.iyaxin.com/
江苏门户网   http://www.jiangsuwang.com.cn/
浙江在线    http://www.zjol.com.cn/
大江网 http://www.jxcn.cn/
荆楚网 http://www.cnhubei.com/
广西新闻网   http://www.gxnews.com.cn/
每日甘肃    http://www.gansudaily.com.cn/
山西新闻网   http://www.sxrb.com/
内蒙古新闻网  http://www.nmgnews.com.cn/
陕西网 http://www.ishaanxi.com/
吉林在线    http://www.jlline.com/
东南网 http://www.fjsen.com/
厦门蓝房网   http://xm.lanfw.com/
多彩贵州网   http://www.gog.cn/
21CN房产频道    http://house.21cn.com/
深圳房地产信息网    http://www.szhome.com/
广东新闻网   http://www.gd.chinanews.com/
中国西藏新闻网 http://www.chinatibetnews.com/
四川新闻网   http://www.newssc.org/
宁夏新闻网   http://www.nxnews.net/
海南网 http://www.hinews.cn/
新浪地产网   http://news.dichan.sina.com.cn/
买房网 http://www.payfang.com/
易铺网 http://yipu.com.cn/
爱易房 http://www.iefang.com/
金华房产    http://www.0579fw.com/
中国商业地产营运门户网 http://www.fip.com.cn/
```

    @todo: 需要总结可能的城市列表

#### 城市列表

national 全国
xiamen 厦门


#### 网站规则

- 新浪厦门

  name: sina_xm
  location: xiamen
  start: http://search.house.sina.com.cn/xm/news/page01/
  page: http://search.house.sina.com.cn/xm/news/page\d+/
  item: http://xm.house.sina.com.cn/news/\d+-\d+-\d+/\d+.shtml


- 中国房地产信息网

  name: cei
  location: national
  start: http://www.realestate.cei.gov.cn/filea/a/xxbr.aspx?p=1&c=
  page: http://www.realestate.cei.gov.cn/filea/a/xxbr.aspx?p=1&c=  # 一共 22 页
  item: http://www.realestate.cei.gov.cn/filea/br.aspx?id=20150109161344

- 搜房房地产

  name: fang
  location: national
  start: http://www.fang.com/news/gdxw/2015-01-14/1.html ## 日期为今天
  page: http://www.fang.com/news/gdxw/2015-01-14/\d+.html
  item: http://www.fang.com/news/\d+-\d+-\d+/\d+\.htm

- 中文房地产网（把对方网站跑挂了）

  name: crb
  location: national
  start: http://www.china-crb.cn/resourcelist.jsp?$CURRPAGE$=1
  page: http://www.china-crb.cn/resourcelist.jsp?$CURRPAGE$={}
  item: http://www.china-crb.cn/resource.jsp?id=25438

- 人民网房产

  name: people
  location: national
  start: http://house.people.com.cn/GB/194441/review/20150114.html # 按日期查询
  page: http://house.people.com.cn/GB/194441/review/{date}.html
  item: http://house.people.com.cn/n/\d{4}/\d{4}/c\d+-\d+\.html

- 凤凰房产

  name: ifeng
  location: national
  start: http://house.ifeng.com/news/policy/0 # 需要分栏目和页码
  page: http://house.ifeng.com/news/policy/\d+
  item: http://house.ifeng.com/detail/2015_01_14/50223586_0.shtml

- 中房网

  name: fangchan
  location: national
  start: http://www.fangchan.com/news/{}/p{}
  page: http://www.fangchan.com/news/{}/p{}
  item:
    - http://www.fangchan.com/news/2015-01-14/5960933308887273536.html
    - http://www.fangchan.com/news/1/2015-01-14/5960938724585181433.html

- 地产中国网

  name: house_china
  location: national
  start: http://house.china.com.cn/News/111_1.htm
  page: http://house.china.com.cn/News/111_\d+.htm
  item: http://house.china.com.cn/home/view/771911.htm

@todo: 房产网站


## 内容处理流程

- 使用 Goose - Article Extractor 提取网页内主要内容部分

https://github.com/grangier/python-goose

实现：
  extract_content.py

问题：
  发现有的网页不能提取出内容，有的网页提取会报错。

  解决：
  - 使用 https://github.com/yono/python-extractcontent
    或 https://github.com/buriy/python-readability
    进行再次处理

  - 如果还不行，则直接剔除 html 标签，保存文本


- 使用 jieba 中文分词库，https://github.com/fxsjy/jieba

  - 只对中文和长度超过 1 的英文单词分词
  - 去掉结果中的数字
  - 结果导出 文档 对应的 词频 json 数据

## 探查 SQL

```

--
select count(id) from estate;1

--
select distinct(website) from estate;

--
select count(id) from estate where website = 'cei';
select count(id) from estate where website = 'house_china';

--
select * from estate where website = 'cei' limit 2;
select * from estate where website = 'fang' limit 2;

--

select * from estate where content is not null limit 50;

--

select * from estate where url = 'http://www.fang.com/news/2014-12-25/14477218.htm'

--
select count(id) from estate where content is not null;

select count(id) from estate where content is null;

select count(id) from estate where content = '[extract_error]';
select count(id) from estate where content = '[no_cleaned_text]';

--
select * from estate where content = '[extract_error]';

delete from estate where id = 2510;

--
select * from estate where content = '[no_cleaned_text]';


```

## 日志

2015-01-14:
  抓取：

  - sina_xm 1012 条
  - cei 843 条
  - fang 1052 条
  - crb  25 条（把对方网站跑挂了）
  - people 2016 条
  - ifeng 2973 条
  - fangchan 3017 条
  - house_china 516 条

  总计：11456 条

  临时状态 status
    - 1 内容提取出错的文档，用readability重新处理，然后用 BS 去掉标签
    - 2 分词出错（没有出错）

  导出 csv，共11445条纪录
    - url
    - website
    - published_at
    - seg_freq

内容提取出错的文档：

('http://www.realestate.cei.gov.cn/filea/br.aspx?id=20150112091744',
'http://www.realestate.cei.gov.cn/filea/br.aspx?id=20150105105810',
'http://www.realestate.cei.gov.cn/filea/br.aspx?id=20150104160449',
'http://www.realestate.cei.gov.cn/filea/br.aspx?id=20150104160511',
'http://www.realestate.cei.gov.cn/filea/br.aspx?id=20150104160534',
'http://www.realestate.cei.gov.cn/filea/br.aspx?id=20150104160554',
'http://www.realestate.cei.gov.cn/filea/br.aspx?id=20150104160628',
'http://www.realestate.cei.gov.cn/filea/br.aspx?id=20150104160652',
'http://www.realestate.cei.gov.cn/filea/br.aspx?id=20150104160712',
'http://www.realestate.cei.gov.cn/filea/br.aspx?id=20150104160727',
'http://www.realestate.cei.gov.cn/filea/br.aspx?id=20150105144903',
'http://www.realestate.cei.gov.cn/filea/br.aspx?id=20150105144941',
'http://www.realestate.cei.gov.cn/filea/br.aspx?id=20150105145009',
'http://www.realestate.cei.gov.cn/filea/br.aspx?id=20150105145040',
'http://www.realestate.cei.gov.cn/filea/br.aspx?id=20150105145130',
'http://www.realestate.cei.gov.cn/filea/br.aspx?id=20150105145223',
'http://www.realestate.cei.gov.cn/filea/br.aspx?id=20150105144635',
'http://www.realestate.cei.gov.cn/filea/br.aspx?id=20150106164222',
'http://www.realestate.cei.gov.cn/filea/br.aspx?id=20150106104317',
'http://www.realestate.cei.gov.cn/filea/br.aspx?id=20150107105119',
'http://www.realestate.cei.gov.cn/filea/br.aspx?id=20150113160440',
'http://www.realestate.cei.gov.cn/filea/br.aspx?id=20150113160547',
'http://www.realestate.cei.gov.cn/filea/br.aspx?id=20150112094408',
'http://www.realestate.cei.gov.cn/filea/br.aspx?id=20150112140435',
'http://www.realestate.cei.gov.cn/filea/br.aspx?id=20150112141206',
'http://www.realestate.cei.gov.cn/filea/br.aspx?id=20150112141152',
'http://www.realestate.cei.gov.cn/filea/br.aspx?id=20150105110450',
'http://www.fang.com/news/2015-01-13/14622636.htm',
'http://www.fang.com/news/2015-01-08/14586210.htm',
'http://www.fang.com/news/2015-01-13/14622635.htm',
'http://www.fang.com/news/2015-01-08/14586326.htm',
'http://www.fang.com/news/2015-01-08/14586789.htm',
'http://www.fang.com/news/2015-01-10/14601476.htm',
'http://www.fang.com/news/2015-01-11/14604034.htm',
'http://www.fang.com/news/2015-01-11/14604278.htm',
'http://www.fang.com/news/2015-01-12/14608086.htm',
'http://www.fang.com/news/2015-01-11/14604984.htm',
'http://www.fang.com/news/2015-01-13/14623401.htm',
'http://www.fang.com/news/2015-01-13/14622638.htm',
'http://www.fang.com/news/2015-01-13/14623362.htm',
'http://www.fang.com/news/2015-01-13/14624572.htm',
'http://www.fang.com/news/2015-01-13/14624812.htm',
'http://www.fang.com/news/2015-01-13/14623153.htm',
'http://www.fang.com/news/2015-01-13/14625044.htm',
'http://www.fang.com/news/2015-01-13/14625456.htm',
'http://www.fang.com/news/2015-01-13/14624525.htm',
'http://www.fang.com/news/2015-01-07/14574818.htm',
'http://www.fang.com/news/2015-01-07/14574822.htm',
'http://www.fang.com/news/2015-01-13/14625168.htm',
'http://www.fang.com/news/2015-01-07/14575190.htm',
'http://www.fang.com/news/2015-01-07/14575373.htm',
'http://www.fang.com/news/2015-01-07/14575608.htm',
'http://www.fang.com/news/2015-01-07/14575616.htm',
'http://www.fang.com/news/2015-01-13/14625532.htm',
'http://www.fang.com/news/2015-01-13/14626017.htm',
'http://www.fang.com/news/2015-01-14/14628909.htm',
'http://www.fang.com/news/2015-01-09/14599123.htm',
'http://www.fang.com/news/2015-01-06/14562587.htm',
'http://www.fang.com/news/2015-01-06/14562628.htm',
'http://www.fang.com/news/2015-01-06/14562577.htm',
'http://www.fang.com/news/2015-01-06/14565039.htm',
'http://www.fang.com/news/2015-01-06/14567443.htm',
'http://www.fang.com/news/2015-01-06/14567231.htm',
'http://www.fang.com/news/2015-01-06/14567479.htm',
'http://www.fang.com/news/2015-01-06/14567518.htm',
'http://www.fang.com/news/2015-01-06/14563222.htm',
'http://www.fang.com/news/2015-01-06/14563431.htm',
'http://www.fang.com/news/2015-01-09/14599240.htm',
'http://www.fang.com/news/2015-01-05/14557530.htm',
'http://www.fang.com/news/2015-01-05/14554813.htm',
'http://www.fang.com/news/2015-01-05/14554712.htm',
'http://www.fang.com/news/2015-01-04/14547965.htm',
'http://www.fang.com/news/2015-01-04/14547771.htm',
'http://www.fang.com/news/2015-01-04/14548166.htm',
'http://www.fang.com/news/2015-01-04/14542424.htm',
'http://www.fang.com/news/2015-01-04/14542562.htm',
'http://www.fang.com/news/2015-01-04/14548690.htm',
'http://www.fang.com/news/2015-01-04/14548810.htm',
'http://www.fang.com/news/2014-12-31/14527611.htm',
'http://www.fang.com/news/2014-12-30/14515255.htm',
'http://www.fang.com/news/2014-12-30/14515508.htm',
'http://www.fang.com/news/2014-12-30/14516418.htm',
'http://www.fang.com/news/2014-12-30/14516529.htm',
'http://www.fang.com/news/2014-12-30/14516612.htm',
'http://www.fang.com/news/2014-12-30/14516990.htm',
'http://www.fang.com/news/2014-12-30/14516951.htm',
'http://www.fang.com/news/2014-12-30/14517035.htm',
'http://www.fang.com/news/2014-12-30/14514911.htm',
'http://www.fang.com/news/2014-12-30/14515186.htm',
'http://www.fang.com/news/2014-12-30/14515187.htm',
'http://www.fang.com/news/2014-12-29/14510448.htm',
'http://www.fang.com/news/2014-12-29/14510738.htm',
'http://www.fang.com/news/2014-12-29/14507505.htm',
'http://www.fang.com/news/2014-12-29/14504982.htm',
'http://www.fang.com/news/2014-12-29/14503428.htm',
'http://www.fang.com/news/2014-12-29/14505379.htm',
'http://www.fang.com/news/2014-12-31/14530900.htm',
'http://www.fang.com/news/2014-12-29/14501638.htm',
'http://www.fang.com/news/2014-12-30/14518521.htm',
'http://www.fang.com/news/2014-12-31/14523639.htm',
'http://www.fang.com/news/2014-12-25/14475840.htm',
'http://www.fang.com/news/2014-12-25/14477218.htm',
'http://www.fang.com/news/2014-12-25/14477537.htm',
'http://www.fang.com/news/2014-12-25/14478855.htm',
'http://www.fang.com/news/2014-12-25/14479172.htm',
'http://www.fang.com/news/2014-12-25/14479159.htm',
'http://www.fang.com/news/2014-12-24/14472095.htm',
'http://www.fang.com/news/2014-12-25/14473965.htm',
'http://www.fang.com/news/2014-12-24/14469077.htm',
'http://www.fang.com/news/2014-12-24/14469197.htm',
'http://www.fang.com/news/2014-12-24/14469230.htm',
'http://www.fang.com/news/2014-12-31/14523765.htm',
'http://www.fang.com/news/2014-12-30/14517084.htm',
'http://www.fang.com/news/2014-12-30/14517396.htm',
'http://www.fang.com/news/2014-12-30/14517471.htm',
'http://www.fang.com/news/2014-12-30/14517452.htm',
'http://www.fang.com/news/2014-12-30/14517665.htm',
'http://www.fang.com/news/2014-12-23/14462037.htm',
'http://www.fang.com/news/2014-12-30/14517623.htm',
'http://www.fang.com/news/2014-12-23/14462057.htm',
'http://www.fang.com/news/2014-12-24/14465444.htm',
'http://www.fang.com/news/2014-12-24/14465957.htm',
'http://www.fang.com/news/2014-12-24/14462921.htm',
'http://www.fang.com/news/2014-12-24/14465231.htm',
'http://www.fang.com/news/2014-12-24/14465374.htm',
'http://www.fang.com/news/2014-12-30/14517705.htm',
'http://www.fang.com/news/2014-12-30/14518378.htm',
'http://www.fang.com/news/2014-12-30/14518372.htm',
'http://www.fang.com/news/2014-12-30/14518391.htm',
'http://www.fang.com/news/2014-12-30/14518383.htm',
'http://www.fang.com/news/2014-12-30/14518381.htm',
'http://www.fang.com/news/2014-12-30/14518722.htm',
'http://www.fang.com/news/2014-12-30/14518825.htm',
'http://www.fang.com/news/2014-12-30/14519032.htm',
'http://www.fang.com/news/2014-12-30/14519023.htm',
'http://www.fang.com/news/2014-12-30/14519096.htm',
'http://www.fang.com/news/2014-12-30/14519426.htm',
'http://www.fang.com/news/2014-12-30/14519060.htm',
'http://www.fang.com/news/2014-12-30/14519516.htm',
'http://www.fang.com/news/2014-12-30/14519535.htm',
'http://www.fang.com/news/2014-12-30/14519769.htm',
'http://www.fang.com/news/2014-12-30/14519556.htm',
'http://www.fang.com/news/2014-12-30/14518368.htm',
'http://www.fang.com/news/2014-12-30/14519817.htm',
'http://www.fang.com/news/2014-12-29/14503426.htm',
'http://www.fang.com/news/2014-12-28/14498643.htm',
'http://www.fang.com/news/2014-12-29/14503386.htm',
'http://www.fang.com/news/2014-12-28/14498862.htm',
'http://www.fang.com/news/2014-12-29/14501208.htm',
'http://www.fang.com/news/2014-12-27/14495597.htm',
'http://www.fang.com/news/2014-12-27/14495609.htm',
'http://www.fang.com/news/2014-12-27/14495675.htm',
'http://www.fang.com/news/2014-12-27/14497250.htm',
'http://www.fang.com/news/2014-12-27/14495751.htm',
'http://www.fang.com/news/2015-01-05/14559064.htm',
'http://www.fang.com/news/2015-01-05/14559093.htm',
'http://www.fang.com/news/2015-01-05/14559051.htm',
'http://www.fang.com/news/2015-01-05/14559173.htm',
'http://www.fang.com/news/2015-01-05/14559425.htm',
'http://www.fang.com/news/2015-01-05/14559533.htm',
'http://www.fang.com/news/2014-12-26/14489537.htm',
'http://www.fang.com/news/2014-12-26/14489534.htm',
'http://www.fang.com/news/2014-12-26/14484261.htm',
'http://www.fang.com/news/2014-12-26/14486098.htm',
'http://www.fang.com/news/2014-12-26/14487176.htm',
'http://www.fang.com/news/2014-12-26/14487210.htm',
'http://www.fang.com/news/2014-12-26/14487721.htm',
'http://www.fang.com/news/2014-12-25/14483183.htm',
'http://www.fang.com/news/2015-01-06/14559964.htm',
'http://www.fang.com/news/2015-01-06/14559965.htm',
'http://www.fang.com/news/2015-01-06/14562523.htm',
'http://www.fang.com/news/2015-01-06/14561564.htm',
'http://www.fang.com/news/2015-01-05/14552692.htm',
'http://www.fang.com/news/2015-01-01/14532802.htm',
'http://www.fang.com/news/2015-01-01/14533723.htm',
'http://www.fang.com/news/2015-01-05/14550246.htm',
'http://www.fang.com/news/2015-01-05/14554611.htm',
'http://www.fang.com/news/2015-01-05/14554941.htm',
'http://www.fang.com/news/2015-01-05/14554900.htm',
'http://www.fang.com/news/2015-01-05/14555400.htm',
'http://www.fang.com/news/2015-01-01/14534569.htm',
'http://www.fang.com/news/2015-01-01/14534002.htm',
'http://www.fang.com/news/2015-01-01/14534573.htm',
'http://www.fang.com/news/2015-01-01/14534596.htm',
'http://www.fang.com/news/2015-01-02/14536581.htm',
'http://www.fang.com/news/2015-01-05/14556614.htm',
'http://www.fang.com/news/2015-01-09/14593442.htm',
'http://www.fang.com/news/2015-01-04/14545973.htm',
'http://www.fang.com/news/2015-01-04/14545886.htm',
'http://www.fang.com/news/2015-01-04/14546627.htm',
'http://www.fang.com/news/2015-01-04/14546657.htm',
'http://www.fang.com/news/2015-01-09/14593487.htm',
'http://www.fang.com/news/2015-01-12/14612075.htm',
'http://www.fang.com/news/2015-01-12/14614248.htm',
'http://www.fang.com/news/2015-01-08/14584741.htm',
'http://www.fang.com/news/2015-01-08/14584951.htm',
'http://www.fang.com/news/2015-01-08/14586092.htm',
'http://www.fang.com/news/2015-01-08/14580710.htm',
'http://www.fang.com/news/2015-01-07/14577538.htm',
'http://www.fang.com/news/2015-01-07/14577751.htm',
'http://www.fang.com/news/2015-01-14/14630577.htm',
'http://www.fang.com/news/2015-01-14/14630815.htm',
'http://www.fang.com/news/2015-01-14/14632307.htm',
'http://www.fang.com/news/2015-01-08/14586122.htm',
'http://www.fang.com/news/2015-01-13/14623756.htm',
'http://www.fang.com/news/2015-01-13/14623644.htm',
'http://www.fang.com/news/2015-01-12/14607938.htm',
'http://www.fang.com/news/2015-01-11/14605731.htm',
'http://www.fang.com/news/2015-01-13/14624496.htm',
'http://www.fang.com/news/2015-01-13/14624442.htm',
'http://www.fang.com/news/2015-01-13/14626019.htm',
'http://www.fang.com/news/2015-01-13/14625742.htm',
'http://www.fang.com/news/2015-01-07/14578629.htm',
'http://www.fang.com/news/2015-01-05/14554868.htm',
'http://www.fang.com/news/2015-01-05/14552689.htm',
'http://www.fang.com/news/2015-01-06/14563314.htm',
'http://www.fang.com/news/2015-01-05/14556599.htm',
'http://www.fang.com/news/2015-01-05/14550145.htm',
'http://www.fang.com/news/2015-01-04/14546015.htm',
'http://www.fang.com/news/2015-01-01/14532875.htm',
'http://www.fang.com/news/2015-01-01/14533466.htm',
'http://www.fang.com/news/2014-12-31/14531200.htm',
'http://www.fang.com/news/2015-01-06/14563765.htm',
'http://www.fang.com/news/2015-01-06/14564503.htm',
'http://www.fang.com/news/2014-12-31/14523778.htm',
'http://www.fang.com/news/2015-01-08/14579108.htm',
'http://www.fang.com/news/2014-12-30/14518672.htm',
'http://www.fang.com/news/2014-12-30/14518599.htm',
'http://www.fang.com/news/2014-12-30/14518758.htm',
'http://www.fang.com/news/2014-12-30/14518800.htm',
'http://www.fang.com/news/2014-12-30/14514649.htm',
'http://www.fang.com/news/2014-12-29/14510396.htm',
'http://www.fang.com/news/2014-12-29/14503341.htm',
'http://www.fang.com/news/2014-12-29/14503383.htm',
'http://www.fang.com/news/2014-12-29/14503427.htm',
'http://www.fang.com/news/2014-12-29/14506004.htm',
'http://www.fang.com/news/2014-12-29/14506127.htm',
'http://www.fang.com/news/2014-12-26/14490717.htm',
'http://www.fang.com/news/2014-12-30/14519629.htm',
'http://www.fang.com/news/2014-12-25/14480449.htm',
'http://www.fang.com/news/2014-12-29/14507495.htm',
'http://www.fang.com/news/2014-12-24/14465933.htm',
'http://www.fang.com/news/2014-12-24/14466074.htm',
'http://www.fang.com/news/2014-12-29/14509148.htm',
'http://www.fang.com/news/2014-12-28/14498587.htm',
'http://www.fang.com/news/2014-12-28/14498868.htm',
'http://www.fang.com/news/2014-12-28/14498878.htm',
'http://www.fang.com/news/2014-12-26/14485848.htm',
'http://www.fang.com/news/2014-12-26/14487208.htm',
'http://www.fang.com/news/2014-12-25/14480214.htm',
'http://www.fang.com/news/2014-12-25/14480443.htm',
'http://www.fang.com/news/2014-12-30/14515268.htm',
'http://www.fang.com/news/2014-12-30/14516812.htm',
'http://www.fang.com/news/2014-12-30/14516563.htm',
'http://www.fang.com/news/2014-12-30/14517009.htm',
'http://www.fang.com/news/2014-12-25/14477223.htm',
'http://www.fang.com/news/2014-12-24/14470395.htm',
'http://www.fang.com/news/2014-12-31/14530874.htm',
'http://www.fang.com/news/2015-01-08/14579111.htm',
'http://www.fang.com/news/2014-12-30/14517436.htm',
'http://www.fang.com/news/2014-12-30/14517580.htm',
'http://www.fang.com/news/2015-01-08/14583746.htm',
'http://www.fang.com/news/2014-12-30/14517533.htm',
'http://www.fang.com/news/2014-12-30/14518511.htm',
'http://www.fang.com/news/2014-12-30/14518532.htm',
'http://www.fang.com/news/2015-01-07/14569991.htm',
'http://house.people.com.cn/n/2015/0105/c164220-26328851.html',
'http://house.people.com.cn/n/2014/1230/c194441-26302522.html',
'http://house.people.com.cn/n/2014/1231/c164220-26309094.html',
'http://house.people.com.cn/n/2015/0101/c164220-26310781.html',
'http://house.people.com.cn/n/2015/0110/c164220-26361363.html',
'http://house.people.com.cn/n/2015/0111/c194441-26362846.html',
'http://house.people.com.cn/n/2015/0113/c194441-26377357.html',
'http://house.people.com.cn/n/2014/1217/c194441-26225578.html',
'http://house.people.com.cn/n/2014/1208/c164220-26169129.html',
'http://house.people.com.cn/n/2014/1115/c164220-26030307.html',
'http://www.fangchan.com/news/2/2013-01-18/340412.html',
'http://www.fangchan.com/news/2/2013-01-18/340413.html')

## Q

- R 中如何读取 json