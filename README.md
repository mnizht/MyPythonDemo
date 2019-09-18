# MyPythonDemo
阿里云Python学习路线

### python优势

作为脚本语言是它比shell脚本适用范围更广，shell脚本最擅长移动文件和替换文件，并不适合GUI界面或者游戏开发。

Python很容易使用，但它是一种真正的编程语言，提供了多种数据结构，也支持大型程序。

Python 允许你划分程序模块，在其它Python程序中重用。

Python 是一种解释型语言，在程序开发阶段可以为你节约大量时间，因为不需要编译和链接。

Python 程序的书写是紧凑而易读的。Python 通常比同样功能的 C, C++, Java 短很多，原因列举如下：

- 高级数据类型允许在一个表达式中表示复杂的操作；
- 代码块的划分是按照缩进而不是成对的花括号；
- 不需要预先定义变量或参数

Python 是“可扩展的”：如果你知道怎么写C语言程序，就能很容易的给解释器添加新的内置函数和模块，不论是让关键额的程序以最高速度运行，还是把Python程序链接到只提供预编译程序的库（比如硬件相关的图形库）。一旦你真正链接上了，就能在Python解释器中扩展或者控制C语言编写的应用了。

**一些基本的语法概念因为与Java差不多，所以就不再重复记录了，下面只记录一些我觉得独特的地方。**

### 注意

Python 运算符的用法和其它大部分语言基本一样（因为本人主要使用Java ，所以之后都用Java 做比较）

- 关于基本数据类型

  - 数字类型：python3有int整数、float浮点数、complex复数（这个Java里是没有的）。以及Decimal(十进制)（对位Java中BigDecimal类型，用于做高精度的浮点运算）， Fraction(分数)（这个Java里也没有）

  ​      在python2时 int整数是有大小限制的，当数字超过一定范围后就不再是int了，而是long型，而在python3中取消了long型，只要是整数一律是int型，所以python3中的整           数是没有大小限制的。

  - boolean类型值，由于Python是大小写敏感的

    ```python
    a = True #True 和 False一定要写成首字母大写
    a = false  # 如果这么写的话，它会人为false是一个变量；编译时没问题，但是执行到这时可能会报 NameError: name 'false' is not defined异常，如果你前面没有定义一						个名为false的变量的话
    ```

  - str字符串类和list类与Java基本用法基本一样。dict(字典)与Java的Map用法看起来也差不多。比较特别的是Python有个 tuple(元组)，它是不可修改的列表，特性与list相似，但是是用圆括号括起来的。

    ```python
    # 元组
    name = ("tom","jerry")
    print(name[0])
    ```

  - 空值

    ```python
    # python 的空值就是None，不是null；注意首字母依然要大写
    b = None
    ```

    

- / 对于这个除法运算符，Java在计算时会根据参与运算的值的类型来决定返回值类型。而Python中永远返回浮点数类型。

  ```java
  int a = 9;
  int b = 2;
  > a / b
  > 4   //由于参与运算的 a 和 b 都是int类型，所以返回值也是int型，此时 / 运算符相当于是取整运算
    
  double x = 9;
  double y = 2;
  > x / y
  > 4.5  // 当运算的值中有double类型时，返回值会变成double类型，此时 / 运算符就是正常的除法运算
  ```

  ```python
  >>> 17 / 3
  5.666666666666667 #python 的 / 运算符返回值是浮点型
  >>> 17 // 3
  5		# 想要取整运算时，需要使用 // 运算符
  ```

- Python 中可以使用 ** 运算符来计算乘方；str * int  会复制字符串

  ```python
  >>> 5 ** 2
  25
  # 因为 ** 比 - 有更高的优先级，所以 -3**2 会被解释成 -(3**2), 因此结果是 -9；为了得到正确的的结果9，需要(-3)**2这样把-3用()包起来
  >>> -3**2
  -9
  >>> (-3)**2
  9
  
  >>> a = 'abc'
  >>> print(a * 3)
  abcabcabc
  ```

- Python 支持使用 + 号来拼接String类型字符串，但与Java不同的是，Python中的 + 号两边的参数只能是字符串类型，如果其中有一个是数字类型会报错，而在Java中，两个参数都会被格式化为String进行拼接。所以Python在打印变量时，尽量不要用 + 号进行拼接。可以使用 ，号分隔常量与参数，或使用占位符 引用多个参数（类似C语言的写法），这种方法参数都可以用 %s 来格式化成String类型，但是不能反过来。也可以使用 f“” 格式化字符串方式。

  ```python
  >>> a = "abc"
  >>> c = 1
  
  >>> print("c = " + c)
  Traceback (most recent call last):
    File "<pyshell#17>", line 1, in <module>
      print("c = " + c)
  TypeError: can only concatenate str (not "int") to str
  >>> print("c = ",c)
  c =  1
  # %s 	字符串填充
  # %f	小数填充
  # %d	整数填充
  
  >>> print("a is %s and c is %d" %(a,c))
  >>>      a is abc and c is 1
  >>> print("a is %s and c is %s" %(a,c))
  >>>      a is abc and c is 1
  >>>
  >>> print("a is %d " %(a))
  >>>      Traceback (most recent call last):
  >>>        File "<pyshell#25>", line 1, in <module>
  >>>          print("a is %d " %(a))
  >>>      TypeError: %d format: a number is required, not str
  
  # %3 表示最少显示3位，若参数不足3位，会在前面补空格； %3.5 表示最少显示3位，最      多显示5位，参数短了补空格，多了截取
  
  >>> print(f'a={a}, and c={c}')
  a=abc, and c=1
  ```

- python的三目运算符

  ```python
  # 语句1 if 条件表达式 else 语句2；  条件表达式为True时返回语句1的结果，否则返回2
  ```

  ```java
  //条件表达式 ? 语句1 : 语句2
  //这个是Java的三目运算符，这里我更喜欢Java的风格，条件在前，结果在后，Python那种写法看起来更像是先有了一个结果才去判断条件
  
  ```

- 条件运算符

  ```python
  >>> print(1<2<3)
  True
  # Python的条件运算符可以连着使用，上例相当于 1<2 and 2<3
  # java 的条件运算符不支持连用，上述写法编译时会报 Operator '<' cannot be applied to 'boolean','int',它是用了1<2的结果去与3比较了
  ```

  

  - 在交互模式下，上一次打印出来的表达式被赋值给变量 _。这意味着当你把Python 当做桌面计算器时，继续计算会相对简单；但是 _ 这个变量应该被使用者当做是只读类型。如果你向它显式的赋值，就会创建一个和它名字相同的本地变量，它会屏蔽内部变量。

    ```python
    >>> 1+1
    2 # 此时结果 2 会被赋值给系统变量 _（姑且先叫它系统变量，为了与之后那个本地变量区分）
    >>> _
    2	# 打印系统变量_ ,可以看到结果是 2
    >>> _ = 4	# 给变量 _ 赋值 4 ，此时会创建一个同名的本地变量 _
    >>> _  # 再次打印变量 _
    4				#结果是 4,因为这时系统变量 _ 已经被屏蔽了
    >>> 1+2	
    3	# 再次执行一个运算，这个结果 3应该被赋给(系统)变量 _
    >>> _
    4	# 打印(本地)变量 _,发现结果依然是4
     # 到这一步我本想把系统变量 _ 也打印出来看看是不是3，但是找不到打印的方法了
    ```

  - Python 的方法中，如果参数用 [] 包起来，表示这个参数是可选的。

  - 花括号或set() 函数可以用来创建集合。但要创建一个空集合时只能用set() 而不能用{}，因为后者是创建一个空字典。

  - 关于注释

    ```java
    // 双斜杠单行注释
    /* 斜杠加* 多行注释，不过一般不怎么用这种
    */
    /**
    * 斜杠加两个 * ，文档注释，常用于解释类或方法
    */
    ```

    ```python
    # 单行注释
    '''
    三个单引号括起来的多行注释
    '''
    """
    三个双引号括起来的多行注释，不过这样的多行注释在编译器里看起来和定义的字符串颜色一样，辨识度不高，介意的话可以自行修改颜色
    """
    ```

- if语句,可以有多个零或多个 elif 部分，以及一个可选的 else 部分。关键字 'elif' 是 'else if' 的缩写，适合用于避免过多的缩进。一个 if ... elif ... elif ... 序列可以看做是其它语言中的 switch 或 case 语句的替代。

  ```python
  >>> x = int(input("Please enter an integer: "))
  Please enter an integer: 42
  >>> if x < 0:
  ...     x = 0
  ...     print('Negative changed to zero')
  ... elif x == 0:
  ...     print('Zero')
  ... elif x == 1:
  ...     print('Single')
  ... else:
  ...     print('More')
  ...
  More
  ```

  ```python
  # 默认情况下，if语句只会控制紧随其后的那条语句，如果希望if可以控制多条语句， 则可以在if后跟着一个代码块
  >>> if x < 0:
  ...     x = 0
  ...     print('Negative changed to zero')
  # 其中 x = 0 和 print语句组成了一个代码块
  # 如果一个if 语句后面直接跟了一条语句，那这个if语句就不能再添加代码块了
  >>> if x < 0: x = 0
  ...			print('Negative changed to zero')  # 这里会编译不通过
  # 编译器格式化代码时，会自动把if语句后紧跟的语句移到下面的代码块里，所以不建议直接在if语句后跟语句
  ```

- python中特有的 for ... else 和 while ... else 语句

  循环语句可能带有一个else子句；它会在循环遍历完列表(使用for)或是条件变为假(使用while)的时候被执行，但是不会在循环被break语句终止时被执行。

  ```pythn
  for n in range(2, 10):
      for x in range(2, n):
          if n % x == 0:
              print(n, 'equals', x, '*', n // x)
              break
      else:
          print(n, 'is a prime number(素数)')
          
  2 is a prime number(素数)
  3 is a prime number(素数)
  4 equals 2 * 2
  5 is a prime number(素数)
  6 equals 2 * 3
  7 is a prime number(素数)
  8 equals 2 * 4
  9 equals 3 * 3
  
  # 可以看到由于else 是属于 第二个for循环的，当for循环通过break终止后，else就不会执行
  ```

- Python的list 列表类型数据类似与Java中的数组与list的合并。

  ```python
  stus = ['孙悟空','猪八戒','沙和尚','唐僧','蜘蛛精','白骨精']
  print(stus[-2])
  > 蜘蛛精
  # python 可以像Java使用数组下标获取元素一样获取list的元素，不过Java的数组和list都不支持负数做下标。而Python支持，负数表示从后向前数第几个。
  ```

- Python3的print方法默认自动换行。不像Java中有 print 和 println可选

  ```python
  # 因为python3中 print 后会自动换行，有时候不想换行的话，就需要加个参数
  print('Hello world')
  print('!')
  >Hello world
  >!
  
  print('Hello world', end=' ')
  print('!')
  >Hello world !
  # print('contents', end='可以填任意字符') 不加end参数的话默认是'\n'换行符
  ```

  

