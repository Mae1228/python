# 京津冀经济圈内35个包裹邮寄目的地汇总
dic = {'河北': {'保定': ['004', '012'], '唐山': ['015', '003', '021'], '廊坊': ['025', '017'],
              '石家庄': ['002', '028', '008'], '秦皇岛': ['006', '007'], '张家口': ['011', '013', '026'],
              '承德': ['024'], '沧州': ['001'], '衡水': ['014', '035'], '邢台': ['009', '016'],
              '邯郸': ['018', '027'], '定州': ['029'], '辛集': ['033']},
       '河南': {'安阳': ['005', '023']},
       '北京': {'北京': ['010', '019', '020', '022', '030', '031']},
       '天津': {'天津': ['032', '035']}}

# 查找“001”号包裹的邮寄目的地
for k, v in dic.items():
    for k1, v1 in v.items():
        if '001' in v1:
            print(k1)


