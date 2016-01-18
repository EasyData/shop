shop
====

- forzieri
  - :us: http://www.forzieri.com/
  - :cn: http://www.cn.forzieri.com/
- shopbop
  - :us: https://www.shopbop.com/
  - :cn: https://cn.shopbop.com/

```bash
$ scrapy list
forzieri_en
forzieri_zh
shopbop_en
shopbop_zh

$ scrapy crawl forzieri_en -o forzieri_en.jl
$ scrapy crawl forzieri_zh -o forzieri_zh.jl
$ scrapy crawl shopbop_en -o shopbop_en.jl
$ scrapy crawl shopbop_zh -o shopbop_zh.jl

$ merge forzieri_*.jl
$ merge shopbop_*.jl
```
