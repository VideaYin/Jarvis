django中的url寻址逻辑：
1、项目的settings.py中指定ROOT_URLCONF，url根目录
2、在backend_cha2_sec2文件夹下的urls.py文件中，include不同的应用级urls配置文件
3、在apis的应用中，指定视图

url的RESTful设计：
get     查询
post    新建
put     更新
delete  删除
