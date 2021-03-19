--python list:
list = ['red', 'green', 'blue', 'yellow', 'white', 'black']
print( list[0] )

--java list:

 ArrayList<String> sites = new ArrayList<String>();
        sites.add("Google");
        sites.add("Runoob");
        sites.add("Taobao");
        sites.add("Weibo");
        for (int i = 0; i < sites.size(); i++) {
            System.out.println(sites.get(i));
        }
*************
--python 无数组:

--java 数组：

	 
方法一：

	 // 数组大小
      int size = 10;
      // 定义数组
      double[] myList = new double[size];
      myList[0] = 5.6;
      myList[1] = 4.5;
      myList[2] = 3.3;
      myList[3] = 13.2;
      myList[4] = 4.0;
      myList[5] = 34.33;
      myList[6] = 34.0;
      myList[7] = 45.45;
      myList[8] = 99.993;
      myList[9] = 11123;

方法二：
	double[] myList = {1.9, 2.9, 3.4, 3.5};

读取数组：
      // 计算所有元素的总和
      double total = 0;
      for (int i = 0; i < size; i++) {
         total += myList[i];
      }
      System.out.println("总和为： " + total);


****************
Java json格式：

JSON 语法规则：

JSON 语法是 JavaScript 对象表示语法的子集。
数据在名称/值对中
数据由逗号分隔
大括号 {} 保存对象
中括号 [] 保存数组，数组可以包含多个对象

json 对象：
{ "name":"菜鸟教程" , "url":"www.runoob.com" }

JSON 数组：
{
"name":"网站",
"num":3,
"sites":[ "Google", "Runoob", "Taobao" ]
}

JSON 数组是对象：
{
    "name":"网站",
    "num":3,
    "sites": [
        { "name":"Google","url":"www.runoob.com"},
        { "name":"Runoob", "url":"www.runoob.com"},
        { "name":"Taobao", "url":"www.runoob.com"}
    ]
}

JSON 数组是多个对象：
{
  "bizNo": "YUEYA210317153411",
  "taskNo": "161588291463299378796",
  "servicePkg": "P210H88201",
  "conSumeList": [
    {
      "serviceType": "33320006",
      "totalAmount": "5000.00",
      "usedTime": "2021-03-17 15:31:11",
      "remainAmount": "3100.00",
      "usedAmount": "120.00"
	},
    {
      "serviceType": "33320001",
      "totalAmount": "1000.00",
      "usedTime": "2021-03-17 15:31:11",
      "remainAmount": "540.00",
      "usedAmount": "290.00"
    },
    {
      "serviceType": "33320005",
      "totalAmount": "2000.00",
      "usedTime": "2021-03-17 15:31:11",
      "remainAmount": "168.00",
      "usedAmount": "310.15"
    }
  ]
}

嵌套 JSON 对象中的数组：

{
    "name":"网站",
    "num":3,
    "sites": [
        { "name":"Google", "info":[ "Android", "Google 搜索", "Google 翻译" ] },
        { "name":"Runoob", "info":[ "菜鸟教程", "菜鸟工具", "菜鸟微信" ] },
        { "name":"Taobao", "info":[ "淘宝", "网购" ] }
    ]
}


接口文档：

[外部系统查询保单状态接口-Post请求]
--调用说明 
项目	描述
URL	/appsvr/health/dentalHealthCare/checkServiceStatus
访问方式	Post
	
--输入说明

入参	描述	类型	是否必录	备注	业务规则
clientName	姓名	String	Y		　
gender	性别	String	Y	F：男，M：女	
certificateType	证件类型	String	Y	1: 身份证	
certificateNo	证件号	String	Y	身份证号	　
birthDay	出生日期	String	Y	yyyy-mm-dd 	　
productCode	产品代码	String	Y		
planCode	险种代码	String 	Y		
queryType	查询类型	String	Y	0/1	　

--	输出说明：
参数名	描述	类型	备注
taskNo	返回唯一标识（queryType类型为1时返回）	String	
isValidPol	是否存在有效齿科产品保单	String	Y/N
effectDate	保单生效时间	String	
endDate	保单到期时间	String	
status 	返回状态("00"正常，"01"异常)	String	
message 	返回消息	String	




接口测试用例：

接口名称	  测试接口	请求方式	测试参数	参数描述	测试标题	前置条件	请求参数	预期结果
外部系统查询保单状态接口	/appsvr/health/dentalHealthCare/checkServiceStatus	post	clientName	姓名	输入有保单的用户姓名，查看是否能查询出保单	其他参数正常，查询类型queryType值为0	"{
  ""clientName"": ""张三"",
  ""gender"": ""F"",
  ""certificateType"": ""1"",
  ""certificateNo"": ""360782199508242558"",
  ""birthDay"": ""1995-08-24"",
  ""productCode"": ""P210"",
  ""planCode"": ""H882"",
  ""queryType"": ""0""
  
}"	"1.不返回唯一标识taskNo
2是否存在有效齿科产品保单isValidPol值为Y
3.返回状态status 值为00
