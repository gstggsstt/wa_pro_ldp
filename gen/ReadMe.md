# PrimKV

## 数据生成器使用方法

将`gen.py`和你的程序放在一起，导入类`generator`。

设置`n`，`k`，以得到一个生成器。

每次调用`gen()`方法会生成一个大小为`(n,k,2)`的`list`。

`generator`可以生成多组数据。

``` python
from gen import generator
g = generator(10,3)
data1 = g.gen()
data2 = g.gen()
```



如果你希望生成器每次都使用相同的随机种子，以便调试，可以使用第三个参数设置随机种子。

``` python
from gen import generator
g = generator(10,3,sd=123)
data1 = g.gen()
data2 = g.gen()
```



同时，每个（如primkv中所述的）用户以概率`P`具有一个属性。

即：

- 有`P`的概率有一个属性表示为`<1,v>`；
- 有`1-P`的概率没有一个属性，表示为`<0,0>`

你可以设置`P`的大小，（默认值为0.7）

这里的P表示对于一个用户而言，他大概有P百分比属性是对应有非零的value，与后面LDP中Perturb的流程无关。

``` python
from gen import generator
g = generator(10,3,P=0.9)
data1 = g.gen()
data2 = g.gen()
```