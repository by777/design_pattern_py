# 面向对象的三大特性

+ 封装（属性和方法）
+ 继承（复用，不想重写，类之间的复用代码）
+ 多态（python本身多态，不需要关心）

# 设计模式分类

+ 创建型模式（5种）：
  **工厂方法模式**，  **抽象方法模式**，  **创建者模式**， 原型模式，  **单例模式**
+ 结构型模式（7种）：
  **适配器模式**，**桥模式**， **组合模式**， 装饰模式， **外观模式**， 享元模式， **代理模式**
+ 行为型模式（11种）：
  解释器模式，  **责任链模式**， 命令模式， 迭代器模式， 中介者模式， 备忘录模式，  **观察者模式**， 状态模式
  **策略模式**， 访问者模式，  **模板方法模式**

# 接口

# 面向对象SOLID原则

+ 开放封闭原则
    + 一个软件实体如类，模块和函数，应该对扩展开放，对修改关闭
+ 里式替换原则
    + 所有引用父类的地方必须能透明的使用其子类对象
+ 依赖倒置原则
    + 高层模块不应该依赖低层模块。细节应该依赖于抽象，总之，针对接口编程
+ 接口隔离原则
    + 使用多个专门的接口，而不使用单一的总接口，即客户端不应该依赖那些它不需要的接口
+ 单一职责原则
    + 一个类只负责一项职责

# 简单工厂模式

不直接向客户端暴露对象的实现细节，
而是通过一个工程类来负责创建产品的实例

+ 角色
    + 工厂角色（Creator）
    + 抽象产品角色（Product）
    + 具体产品角色（Concrete Product)

# 工厂方法模式

内容：定义一个用于创建对象的接口（工厂接口），让子类决定去实例化哪一个产品类
角色：

+ 抽象工厂角色（Creator）
+ 具体工厂角色（Concrete Creator）
+ 抽象产品角色（Product）
+ 具体产品角色（Concrete Product)

# 抽象工厂摸索

定义一个工厂类接口，让工厂子类来创建一系列相关或互相依赖的对象。

例如生产一个手机，需要手机壳、cpu和操作系统，每种对象都有不同的种类。
对每个具体工厂，分别生产一部手机所需要的三个对象

相比于工厂方法模式，抽象工厂模式中的每个具体工厂都生产一套产品。

# 建造者模式

建造者模式，将一个复杂对象的构建与表示相分离，使得同样的构建过程可以创建不同的表示
和抽象工厂模式比较相似，也用来创建一个复杂对象。
主要区别是建造者模式着重一步一步构造一个复杂对象，而抽象工厂模式着重于对个系列的产品对象。

角色：

* 抽象建造者-Builder
* 具体建造者-Concrete Builder
* 指挥者-Director
* 产品-Product

# 单例模式

保证一个类只有一个实例，并提供一个访问它的全局访问点
对唯一实例受控访问
单例相当于全局变量，但防止了命名空间被污染

# 适配器模式

内容：将一个类的接口转换成客户希望的了另一个接口。适配器模式使得原本由于借口不兼容而不能一起工作的那些类可以一起工作。

两种实现模式：

+ 类适配器：使用多继承（java不支持多继承）
+ 对象适配器：使用组合

角色：

+ 目标接口（Target）- Payment
+ 待适配的类（Adapted）- ApplePay / BankPay
+ 适配器（Adapter）- PaymentAdapter

# 桥模式

内容：
将一个事物的两个唯独分离，使其可以独立的发生变化

# 组合模式

把对象组合成树形结构以表示“部分-整体“的层次结构。组合模式使得用户对但个对象和组合对象的使用具有一致性
角色：

+ 抽象组件（Component）
+ 叶子组件（Leaf）
+ 复合组件（Composite）
+ 客户端（Client）

# 外观模式

内容：为子系统中的一组接口提供一个一致的界面，外观模式定义了一个高层接口，这一接口使得这一子系统更加容易使用。
角色：

+ 外观（facade）
+ 子系统类（subsystem classes）

# 代理模式

内容：
为其它对象提供一种代理以控制对这个对象的访问
应用场景：

+ 远程代理：为远程的对象提供代理 - 对象（数据）另一个服务器上，如远程数据库对象
+ 虚代理：根据需要创建很大的对象 - 如无图模式用一个方框代替图片
+ 保护代理：控制对原始对象的访问，用于对象有不同的访问权限时

# 责任链模式

内容：
使多个对象都有机会处理请求，从而避免请求的发送者和接收者之间的耦合关系。
将这些对象连成一条链，并沿着这条链传递请求，直到有一个对象处理它为止
角色：

+ 抽象处理者（Handler）
+ 具体处理者（ConcreteHandler）
+ 客户端（Client）

# 观察者模式

内容：定义对象间的一种一对多的依赖关系，当一个对象的状态发生变化时，所有依赖它的对象都得到通知并自动更新。
观察者模式又称为发布-订阅模式
角色：

+ 抽象主题（Subject）
+ 具体主题（ConcreteSubject）- 发布者
+ 抽象观察者（Observer）
+ 具体观察者（ConcreteObserver）- 订阅者

# 策略模式

内容：
定义一系列的算法，把它们一个个封装起来，并使它门可相互替换。
本模式使得算法可以独立于使用它的客户而变化

角色：

+ 抽象策略（Strategy）
+ 具体策略（ConcreteStrategy）
+ 上下文（Context）

# 模板方法模式

内容：
定义了一个操作中算法的骨架，而将一些步骤延迟到子类中。
模板方法使得子类可以不改变一个算法的结构即可重定义该算法的特定步骤
角色：

+ 抽象类：定义抽象的原子操作（钩子操作）；实现一个模板方法作为算法的骨架
+ 具体类：实现原子操作