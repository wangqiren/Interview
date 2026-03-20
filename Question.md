# 🎯 Java 研发工程师面试题库

> **作者**：王启人  
> **岗位**：Java 研发工程师  
> **经验**：7 年  
> **期望薪资**：12K  
> **技术栈**：Java · Spring全家桶 · SpringCloud · MySQL · Redis · MongoDB · RocketMQ · Go  
> **所在地**：沈阳

---

## 📋 目录

- [一、Java 基础与核心](#一java-基础与核心)
- [二、JVM 与性能调优](#二jvm-与性能调优)
- [三、Java 并发编程](#三java-并发编程)
- [四、Spring / SpringMVC / SpringBoot](#四spring--springmvc--springboot)
- [五、Spring Cloud 微服务](#五spring-cloud-微服务)
- [六、MySQL 与数据库调优](#六mysql-与数据库调优)
- [七、Redis 缓存与高可用](#七redis-缓存与高可用)
- [八、MongoDB 与分布式存储](#八mongodb-与分布式存储)
- [九、RocketMQ 消息中间件](#九rocketmq-消息中间件)
- [十、分布式系统与架构设计](#十分布式系统与架构设计)
- [十一、安全开发与 API 安全](#十一安全开发与-api-安全)
- [十二、项目实战与场景题](#十二项目实战与场景题)
- [十三、设计模式](#十三设计模式)
- [十四、Go 语言](#十四go-语言)
- [十五、DevOps 与工程化](#十五devops-与工程化)
- [十六、网络协议基础](#十六网络协议基础)
- [十七、持久层框架](#十七持久层框架)
- [十八、PostgreSQL 数据库](#十八postgresql-数据库)
- [十九、Elasticsearch 全文检索](#十九elasticsearch-全文检索)
- [二十、数据结构与算法](#二十数据结构与算法)
- [二十一、综合软实力与项目管理](#二十一综合软实力与项目管理)

---

## 一、Java 基础与核心

### 1.1 基本概念

#### 1. Java 中 `==` 和 `equals()` 的区别是什么？`String` 类中的 `equals()` 做了什么？

**`==` 比较**：
- 基本类型：比较的是**值**
- 引用类型：比较的是**内存地址**（对象引用是否相同）

**`equals()` 方法**：
- Object 类的默认实现：和 `==` 一样，比较内存地址
- String 类重写了 `equals()`：比较的是**内容是否相同**

```java
String s1 = new String("hello");
String s2 = new String("hello");
s1 == s2;        // false，内存地址不同
s1.equals(s2);  // true，内容相同
```

**String equals() 源码分析**：
```java
public boolean equals(Object anObject) {
    if (this == anObject) return true;  // 地址相同直接返回true
    if (anObject instanceof String) {     // 类型判断
        String anotherString = (String)anObject;
        int n = value.length;
        if (n == anotherString.value.length) {
            // 逐字符比较
            char v1[] = value;
            char v2[] = anotherString.value;
            int i = 0;
            while (n-- != 0) {
                if (v1[i] != v2[i]) return false;
                i++;
            }
            return true;
        }
    }
    return false;
}
```

---

#### 2. 什么是自动装箱与拆箱？`Integer` 缓存池的范围是多少？

**装箱**：将基本类型转换为包装类（调用 `valueOf()`）
**拆箱**：将包装类转换为基本类型（调用 `xxxValue()`）

```java
Integer a = 100;  // 自动装箱，等价于 Integer.valueOf(100)
int b = a;        // 自动拆箱，等价于 a.intValue()
```

**Integer 缓存池**：
- 范围：**-128 到 127**（默认值，可通过 `-XX:AutoBoxCacheMax` 配置）
- 原理：`Integer.valueOf()` 方法会先检查是否在缓存范围内，如果是则直接返回缓存对象

```java
Integer a = 127;
Integer b = 127;
System.out.println(a == b);  // true，命中缓存

Integer c = 128;
Integer d = 128;
System.out.println(c == d);  // false，超出缓存范围，新创建对象
```

**为什么这样设计**：
1. **性能优化**：-128~127 是最常用的整数范围，复用对象减少内存分配和 GC 开销
2. **JLS 规范要求**：Java 语言规范要求此范围内的装箱必须复用对象

---

#### 3. `final`、`finally`、`finalize` 三者的区别？

| 关键字 | 作用 | 特点 |
|--------|------|------|
| `final` | 修饰类/方法/变量 | 类不可被继承、方法不可被重写、变量不可变 |
| `finally` | 异常处理块 | 无论是否异常都会执行（除非 JVM 退出） |
| `finalize` | Object 方法 | 对象被回收前会调用，已不推荐使用 |

**注意**：
- `finally` 中 return 会覆盖 try 中的 return
- `finalize()` 性能差且不可靠，不推荐使用

---

#### 4. Java 中的四种引用类型？

| 引用类型 | 回收时机 | 使用场景 |
|----------|----------|----------|
| 强引用 | JVM 不会回收 | 普通对象引用 |
| 软引用 | 内存不足时回收 | 缓存 |
| 弱引用 | 下次 GC 时回收 | ThreadLocal、缓存 |
| 虚引用 | 随时可能回收 | 跟踪对象被销毁 |

```java
// 软引用缓存示例
SoftReference<byte[]> cache = new SoftReference<>(new byte[1024*1024*10]);
if (cache.get() != null) {
    // 对象未被回收
} else {
    // 重新加载
}
```

---

#### 5. `String`、`StringBuilder`、`StringBuffer` 的区别？

| 特性 | String | StringBuilder | StringBuffer |
|------|--------|---------------|--------------|
| 可变性 | 不可变 | 可变 | 可变 |
| 线程安全 | 安全 | 不安全 | 安全 |
| 性能 | 拼接低 | 高 | 中 |
| 存储 | `final char[]` | `char[]` | `char[]` |

**String 为什么不可变**：
- `private final char value[]` 字段
- 没有提供修改数组的公开方法
- 任何修改都返回新对象

**使用场景**：
- String：字符串常量、配置信息
- StringBuilder：单线程字符串拼接（循环中）
- StringBuffer：多线程字符串操作（历史兼容，现在较少用）

---

#### 6. `hashCode()` 和 `equals()` 的关系？

**hashCode() 通用约定**：
1. 同一对象多次调用返回相同整数（前提：equals 比较的信息未修改）
2. `equals()` 相等的对象必须有相同的 `hashCode()`
3. `equals()` 不相等的对象不要求 hashCode 不同，但最好不同

**如果只重写 equals() 不重写 hashCode()**：
- HashSet/HashMap 会把逻辑相等的对象放到不同桶
- 导致集合无法正确去重、查找失败

---

#### 7. Java 静态代码块、构造代码块、构造方法的执行顺序？

```java
public class Test {
    static {
        System.out.println("1. 静态代码块");
    }
    {
        System.out.println("2. 构造代码块");
    }
    public Test() {
        System.out.println("3. 构造方法");
    }
}
```

**执行顺序**：
```
父类静态代码块 → 子类静态代码块 → 父类构造代码块 → 父类构造方法 → 子类构造代码块 → 子类构造方法
```

---

#### 8. 接口和抽象类的区别？Java 8 之后接口有哪些变化？

| 区别 | 接口 | 抽象类 |
|------|------|--------|
| 继承 | 多继承 | 单继承 |
| 方法 | 抽象方法（Java 8+ 默认/静态） | 抽象+普通方法 |
| 字段 | 常量（static final） | 普通字段 |
| 构造 | 无 | 有 |

**Java 8+ 接口新特性**：
- **默认方法**（default）：接口可以有默认实现
- **静态方法**（static）：接口可以定义静态方法
- **私有方法**（private，Java 9+）：接口内部私有方法

```java
public interface MyInterface {
    // 抽象方法
    void method1();
    
    // 默认方法
    default void method2() {
        System.out.println("默认实现");
    }
    
    // 静态方法
    static void method3() {
        System.out.println("静态方法");
    }
}
```

---

#### 9. 什么是深拷贝和浅拷贝？

- **浅拷贝**：只复制引用，不复制引用指向的对象
- **深拷贝**：复制对象本身及所有引用的对象

```java
// 深拷贝实现方式
class Person implements Cloneable {
    private String name;
    private Address address;
    
    @Override
    public Person clone() {
        Person p = (Person) super.clone();
        p.address = this.address.clone();  // 手动深拷贝
        return p;
    }
}
```

---

#### 10. `try-with-resources` 的原理？

自动资源管理，要求资源实现 `AutoCloseable` 接口

```java
try (FileReader fr = new FileReader("file.txt")) {
    // 使用资源
} // 自动调用 fr.close()
```

---

### 1.2 集合框架

#### 11. `ArrayList` 和 `LinkedList` 的区别？

| 特性 | ArrayList | LinkedList |
|------|------------|-------------|
| 底层 | 动态数组 | 双向链表 |
| 随机访问 | O(1) | O(n) |
| 插入/删除 | O(n) | O(1)（首尾） |
| 内存 | 连续空间 | 额外指针开销 |
| 适用场景 | 随机访问多 | 插入删除多 |

**ArrayList 扩容机制**：
- 默认容量：10
- 扩容公式：`newCapacity = oldCapacity + (oldCapacity >> 1)`（1.5倍）
- 使用 `Arrays.copyOf()` 扩容

---

#### 12. HashMap 的底层数据结构？

**Java 7**：数组 + 链表（头插法）
**Java 8+**：数组 + 链表 + 红黑树（尾插法）

**链表转红黑树条件**：
- 链表长度 > 8
- 且数组长度 >= 64

**红黑树转链表**：
- 节点数 < 6

---

#### 13. HashMap 的 put() 流程？

```
1. 计算 key 的 hash 值（扰动函数）
2. 计算数组下标 (n-1) & hash
3. 如果数组位置为空，直接创建节点放入
4. 如果不为空：
   a. key 相同 → 覆盖 value
   b. key 不同 → 遍历链表/红黑树
   c. 链表长度 > 8 → 转为红黑树
5. 检查是否扩容
```

---

#### 14. HashMap 为什么容量必须是 2 的幂次方？

- 计算下标：`index = (n - 1) & hash`
- 2 的幂次方 - 1 的二进制全是 1，可以完美散列
- 扩容时方便：`newIndex = oldIndex` 或 `oldIndex + oldCap`

---

#### 15. HashMap 负载因子为什么是 0.75？

- 空间和时间成本平衡
- 0.75：空间利用率较高，且 hash 冲突概率较低
- 源码注释：泊松分布计算，8个节点的概率约 0.00000006

---

#### 16. HashMap 在多线程下的问题？

**JDK 7 死循环**：
- 头插法 + 扩容 + 并发 → 链表环形 → 死循环

**JDK 8+ 改进**：
- 尾插法，避免环形链表
- 但仍不保证线程安全

**并发问题**：
- 数据覆盖
- 容量为奇数导致 hash 碰撞
- size 计算不准确

---

#### 17. ConcurrentHashMap 的实现原理？

**Java 7**：Segment 分段锁（每个 Segment 继承 ReentrantLock）
**Java 8+**：CAS + synchronized

```
JDK 7: Segment[] → HashEntry[] → 链表
JDK 8: Node[] → CAS保证安全 → synchronized锁头节点 → 红黑树
```

**CAS 操作用于**：
- 数组初始化
- 扩容时设置当前位置
- 链表转红黑树

**synchronized 用于**：
- 锁住当前节点（头节点）
- 保证节点操作的原子性

---

#### 18. LinkedHashMap 如何实现 LRU 缓存？

```java
class LRUCache<K, V> extends LinkedHashMap<K, V> {
    private final int capacity;
    
    public LRUCache(int capacity) {
        super(16, 0.75f, true);  // accessOrder = true
        this.capacity = capacity;
    }
    
    @Override
    protected boolean removeEldestEntry(Map.Entry<K, V> eldest) {
        return size() > capacity;
    }
}
```

---

### 1.3 泛型与注解

#### 19. Java 泛型的类型擦除？

编译时擦除类型参数，运行时不保留泛型信息

```java
List<String> list = new ArrayList<>();
// 编译后：List list = new ArrayList();
// 实际类型：String 被擦除为 Object
```

**类型擦除的局限**：
- 无法创建泛型数组：`new T[]` 不行
- 无法实例化泛型：`new T()` 不行
- 无法使用基本类型：`List<int>` 不行
- 无法重载泛型方法（类型擦除后签名相同）

---

#### 20. PECS 原则（Producer Extends, Consumer Super）？

- **生产者**（读取数据）：用 `<? extends T>`
- **消费者**（写入数据）：用 `<? super T>`
- 既读又写：不用通配符

```java
// 生产者：只读
List<? extends Number> numbers = new ArrayList<Integer>();
Number n = numbers.get(0);  // 可以

// 消费者：只写
List<? super Integer> numbers = new ArrayList<Number>();
numbers.add(100);  // 可以

// 玉米定理：PECS = Producer Extends, Consumer Super
```

---

#### 21. 注解的 @Retention 区别？

| 级别 | 作用 |
|------|------|
| SOURCE | 编译时丢弃（@Override） |
| CLASS | 编译时保留，运行时丢弃（默认） |
| RUNTIME | 运行时保留（可通过反射读取） |

---

### 1.4 异常处理

#### 22. Error 和 Exception 的区别？

- **Error**：JVM 错误，无法捕获（OutOfMemoryError）
- **Exception**：程序异常，可以捕获处理

**RuntimeException vs Checked Exception**：
- RuntimeException：编译器不强制处理（NullPointerException）
- Checked Exception：编译器强制处理（IOException）

---

#### 23. finally 中有 return 会怎样？

```java
try {
    return 1;
} finally {
    return 2;  // 最终返回 2
}
```

**原则**：不要在 finally 中 return

---

### 1.5 Java 8+ 新特性

#### 24. Stream 的常用操作？

**中间操作**（返回 Stream）：
- `map`、`filter`、`flatMap`、`distinct`、`sorted`、`limit`、`skip`

**终端操作**（返回结果）：
- `collect`、`forEach`、`reduce`、`count`、`anyMatch`、`allMatch`

**map vs flatMap**：
```java
// map: 一对一
list.stream().map(s -> s.length())  // Stream<Integer>

// flatMap: 一对多
list.stream().flatMap(s -> Arrays.stream(s.split("")))  // Stream<String>
```

---

#### 25. Optional 的作用？

避免 NullPointerException

```java
// 传统写法
if (user != null && user.getAddress() != null) {
    String city = user.getAddress().getCity();
}

// Optional 写法
String city = Optional.ofNullable(user)
    .map(User::getAddress)
    .map(Address::getCity)
    .orElse("未知");
```

---

#### 26. Lambda 表达式与函数式接口？

**函数式接口**：只有一个抽象方法的接口

```java
@FunctionalInterface
interface MyFunc {
    void doSomething(String s);
}

// 使用
MyFunc f = s -> System.out.println(s);
f.doSomething("hello");
```

**常见函数式接口**：
- `Function<T,R>`：T→R
- `Predicate<T>`：T→boolean
- `Consumer<T>`：T→void
- `Supplier<T>`：()→T

---

### 1.6 Java IO / NIO

#### 27. BIO、NIO、AIO 的区别？

| 模型 | 阻塞 | 线程模型 | 适用场景 |
|------|------|----------|----------|
| BIO | 阻塞 | 一请求一线程 | 连接数少 |
| NIO | 非阻塞 | 多路复用 | 高并发 |
| AIO | 异步 | 回调 | 异步IO |

**NIO 三大组件**：
- **Channel**：通道（SelectableChannel、FileChannel）
- **Buffer**：缓冲区（ByteBuffer、CharBuffer）
- **Selector**：多路复用器

---

#### 28. ByteBuffer 的 position、limit、capacity？

```java
// 写入模式
buffer.position();    // 当前读写位置
buffer.limit();       // 有效数据终点
buffer.capacity();    // 容量

// flip() 切换为读模式
buffer.flip();  // limit = position, position = 0
```

---

#### 29. 什么是零拷贝？

传统拷贝：用户空间 ↔ 内核空间 ↔ 磁盘
零拷贝：直接在内核空间传输

```java
// FileChannel.transferTo 实现零拷贝
FileChannel.from = new FileInputStream("file").getChannel();
FileChannel.to = new FileOutputStream("file2").getChannel();
from.transferTo(0, from.size(), to);
```

---

### 1.7 Java 反射与动态代理

#### 30. 反射的核心类有哪些？

- `Class`：类本身
- `Field`：属性
- `Method`：方法
- `Constructor`：构造方法

**获取 Class 对象**：
```java
// 方式1
Class<?> clazz = Class.forName("com.example.User");

// 方式2
Class<?> clazz = User.class;

// 方式3
Class<?> clazz = user.getClass();
```

---

#### 31. 反射为什么慢？如何优化？

1. **方法内联**：反射调用无法内联
2. **权限检查**：setAccessible(true) 可跳过检查
3. **参数包装**：可变参数需要数组包装

**优化方案**：
- `setAccessible(true)` 跳过安全检查
- 使用 `MethodHandle`（Java 7+）
- 缓存 Method/Constructor 对象

---

#### 32. JDK 动态代理 vs CGLIB？

| 对比 | JDK 动态代理 | CGLIB |
|------|-------------|-------|
| 原理 | 继承 Proxy 类 | 继承目标类 |
| 限制 | 必须实现接口 | 不能代理 final 类/方法 |
| 性能 | Java 8+ 已优化 | 较高 |
| 生成 | 运行时生成 | 编译期生成 |

---

### 1.8 Java 序列化

#### 33. 常见序列化框架对比？

| 框架 | 格式 | 优点 | 缺点 |
|------|------|------|------|
| JSON | 文本 | 跨语言、可读性好 | 体积大、慢 |
| Jackson | JSON | 性能好、功能全 | - |
| FastJSON | JSON | 快 | 安全漏洞 |
| Protobuf | 二进制 | 体积小、快 | 需要 IDL |
| Kryo | 二进制 | 快 | 跨语言差 |
| JDK | 二进制 | Java 原生 | 慢、不跨语言 |

---

## 二、JVM 与性能调优

### 2.1 内存结构

#### 1. JVM 内存区域有哪些？

| 区域 | 线程私有/共享 | 存储内容 |
|------|-------------|----------|
| 程序计数器 | 私有 | 字节码行号 |
| 虚拟机栈 | 私有 | 方法栈帧（局部变量、操作数栈） |
| 本地方法栈 | 私有 | Native 方法 |
| 堆 | 共享 | 对象实例、数组 |
| 方法区 | 共享 | 类信息、常量、静态变量 |

---

#### 2. Java 8 元空间和 PermGen 区别？

| 特性 | PermGen | Metaspace |
|------|---------|------------|
| 位置 | 堆内存 | 本地内存 |
| 大小 | 固定，难以调整 | 可动态扩展 |
| OOM | PermGen OOM | Metaspace OOM |
| 字符串常量 | 在 PermGen | 移到堆中 |

---

#### 3. 对象创建过程？

```
1. 检查类是否加载（常量池 → 类加载器）
2. 分配内存（指针碰撞 / 空闲列表）
3. 初始化零值
4. 设置对象头
5. 执行 <init> 方法
```

---

#### 4. 什么是逃逸分析？

分析对象作用域，判断是否逃逸出方法/线程

**逃逸优化**：
- **栈上分配**：不逃逸的对象在栈上分配
- **标量替换**：不逃逸的对象拆散为标量

```java
// 逃逸分析示例
public StringBuffer escape() {
    StringBuffer sb = new StringBuffer();  // 逃逸
    return sb;
}

public void noEscape() {
    StringBuffer sb = new StringBuffer();  // 不逃逸，可栈上分配
    sb.append("a");
}
```

---

### 2.2 垃圾回收

#### 5. 垃圾回收算法？

| 算法 | 优点 | 缺点 |
|------|------|------|
| 标记-清除 | 简单 | 内存碎片 |
| 标记-整理 | 无碎片 | 效率低 |
| 复制 | 效率高 | 浪费空间 |
| 分代收集 | 综合最优 | - |

---

#### 6. 常见垃圾回收器？

| 回收器 | 特点 | 适用场景 |
|--------|------|----------|
| Serial | 单线程 | 客户端 |
| ParNew | 多线程 | CMS 配合 |
| Parallel | 吞吐量优先 | 后台批处理 |
| CMS | 并发收集 | 响应时间优先 |
| G1 | 区域化 | 大堆、响应时间 |
| ZGC | 低延迟 | TB级堆 |

---

#### 7. G1 回收器原理？

**Region**：将堆划分为大小相等的 Region

**Young GC**：年轻代回收
**Mixed GC**：年轻代 + 部分老年代

**三色标记**：
1. 白色：未被扫描
2. 灰色：正在扫描
3. 黑色：已扫描完成

---

#### 8. 什么是 STW？

Stop-The-World：GC 时暂停所有工作线程

**减少 STW**：
- G1/ZGC 并发标记
- 合理设置堆大小
- 选择合适的 GC 器

---

### 2.3 类加载机制

#### 9. 类加载过程？

```
加载 → 验证 → 准备 → 解析 → 初始化 → 使用 → 卸载
```

- **加载**：加载 .class 文件
- **验证**：字节码校验
- **准备**：分配内存、设默认值
- **解析**：符号引用 → 直接引用
- **初始化**：执行 <clinit>

---

#### 10. 双亲委派模型？

```
Bootstrap ClassLoader
    ↑
Extension ClassLoader
    ↑
Application ClassLoader
    ↑
自定义 ClassLoader
```

**委派流程**：优先让父加载器尝试加载

**打破场景**：
- SPI（JDBC）
- Tomcat
- 热部署

---

### 2.4 JVM 调优实战

#### 11. 常用 JVM 参数？

```bash
# 堆内存
-Xms512m -Xmx512m          # 初始/最大堆
-XX:NewRatio=2             # 新生代:老年代 = 1:2
-XX:SurvivorRatio=8        # Eden:Survivor = 8:1

# 垃圾回收器
-XX:+UseG1GC               # 使用 G1
-XX:MaxGCPauseMillis=200  # 最大停顿时间

# 元空间
-XX:MetaspaceSize=256m
-XX:MaxMetaspaceSize=512m
```

---

#### 12. OOM 如何排查？

**步骤**：
1. `jps -l` 查看进程
2. `jmap -heap <pid>` 查看堆信息
3. `jmap -dump:format=b,file=heap.hprof <pid>` 导出 dump
4. MAT / JProfiler 分析

**常见 OOM**：
- Heap OOM：对象过多
- Metaspace OOM：类过多
- DirectBuffer OOM：NIO 堆外内存

---

## 三、Java 并发编程

### 3.1 线程基础

#### 1. 线程状态转换？

```
NEW → RUNNABLE → BLOCKED/WAITING/TIMED_WAITING → TERMINATED
```

- NEW：创建未启动
- RUNNABLE：运行中/就绪
- BLOCKED：阻塞（等待锁）
- WAITING：无限等待（wait/join）
- TIMED_WAITING：限时等待（sleep）

---

#### 2. sleep() 和 wait() 的区别？

| 特性 | sleep | wait |
|------|-------|------|
| 所属 | Thread | Object |
| 锁 | 不释放 | 释放 |
| 唤醒 | 自动 | notify |
| 位置 | 任意位置 | synchronized 内 |

---

#### 3. notify() 和 notifyAll() 的区别？

- `notify()`：唤醒一个等待线程（不确定唤醒哪个）
- `notifyAll()`：唤醒所有等待线程

**使用场景**：
- 单一条件：`notify()`
- 多条件：`notifyAll()`（防止死锁）

---

### 3.2 锁机制

#### 4. synchronized 底层原理？

```java
// 字节码层面
public synchronized void method();
  // 方法头：ACC_SYNCHRONIZED

public void syncBlock() {
    synchronized(this) {
        // monitorenter
        // ...
        // monitorexit
    }
}
```

**Monitor 结构**：
- Owner：持有锁线程
- WaitSet：等待队列
- EntryList：阻塞队列

---

#### 5. 锁升级过程？

```
无锁 → 偏向锁 → 轻量级锁 → 重量级锁
```

- **偏向锁**：首次访问，Mark Word 记录线程ID
- **轻量级锁**：CAS 替换 Mark Word
- **重量级锁**：互斥锁，阻塞等待

**不可逆**：只能升级，不能降级

---

#### 6. ReentrantLock 和 synchronized 的区别？

| 特性 | synchronized | ReentrantLock |
|------|--------------|---------------|
| 语法 | 关键字 | API |
| 公平锁 | 不支持 | 支持 |
| 尝试获取锁 | 不支持 | tryLock() |
| 条件变量 | 不支持 | Condition |
| 自动释放 | 是 | finally 手动 |

---

### 3.3 AQS

#### 7. AQS 核心原理？

```java
// 核心变量
private volatile int state;      // 同步状态
private final Node head;        // 头节点
private final Node tail;        // 尾节点
```

**CLH 队列**：双向链表，FIFO

**Node 状态**：
- SIGNAL：需要唤醒
- CANCELLED：已取消
- CONDITION：等待条件
- PROPAGATE：传播

---

#### 8. CountDownLatch、CyclicBarrier、Semaphore？

| 工具 | 作用 | 区别 |
|------|------|------|
| CountDownLatch | 倒计时 | 不可重置 |
| CyclicBarrier | 栅栏 | 可重置 |
| Semaphore | 信号量 | 限流 |

```java
// CountDownLatch：等待 N 个线程完成
CountDownLatch latch = new CountDownLatch(3);
latch.await();  // 等待
latch.countDown();  // 计数-1

// CyclicBarrier：等待 N 个线程到达
CyclicBarrier barrier = new CyclicBarrier(3);
barrier.await();  // 等待所有线程到达

// Semaphore：限流
Semaphore sem = new Semaphore(3);
sem.acquire();  // 获取许可
sem.release();  // 释放许可
```

---

### 3.4 线程池

#### 9. 线程池工作流程？

```
1. 线程数 < corePoolSize → 创建核心线程
2. 线程数 >= corePoolSize → 加入队列
3. 队列满 → 创建临时线程（至 maxPoolSize）
4. 临时线程满 → 拒绝策略
```

---

#### 10. 线程池拒绝策略？

| 策略 | 行为 |
|------|------|
| AbortPolicy | 抛异常 |
| CallerRunsPolicy | 调用者执行 |
| DiscardPolicy | 丢弃 |
| DiscardOldestPolicy | 丢弃最老任务 |

---

#### 11. 为什么不推荐 Executors 创建线程池？

```java
// 问题：使用无界队列，可能 OOM
Executors.newFixedThreadPool(100);  // LinkedBlockingQueue

// 正确方式
new ThreadPoolExecutor(
    10, 
    100, 
    60L, TimeUnit.SECONDS,
    new LinkedBlockingQueue<>(1000),
    new ThreadPoolExecutor.AbortPolicy()
);
```

---

#### 12. ThreadLocal 内存泄漏？

**原因**：ThreadLocalMap 使用弱引用，但 Entry 持有 value 强引用

**解决**：
- 使用完 remove()
- 使用 InheritableThreadLocal 替代（谨慎）

```java
// 最佳实践
try {
    threadLocal.set(value);
    // 使用
} finally {
    threadLocal.remove();
}
```

---

### 3.5 并发工具类

#### 13. volatile 的作用？

1. **可见性**：一个线程修改，其他线程立即可见
2. **禁止指令重排序**

**内存屏障**：
- Load 屏障：读取最新值
- Store 屏障：写入主内存

**不能保证原子性**：
```java
volatile int count = 0;
count++;  // 不是原子操作（read-increment-write）
```

---

#### 14. CAS 的原理和 ABA 问题？

**CAS**：Compare And Swap

```java
// 伪代码
boolean compareAndSwap(int expected, int newValue) {
    if (current == expected) {
        current = newValue;
        return true;
    }
    return false;
}
```

**ABA 问题**：A → B → A，CAS 无法感知

**解决**：使用 `AtomicStampedReference`（带版本号）

---

#### 15. LongAdder 相比 AtomicLong？

```java
// AtomicLong：单个 CAS 操作
AtomicLong count = new AtomicLong();
count.incrementAndGet();

// LongAdder：分段 CAS，减少冲突
LongAdder count = new LongAdder();
count.increment();
long sum = count.sum();
```

**适用场景**：
- AtomicLong：高并发读
- LongAdder：高并发写（累加器）

---

## 四、Spring / SpringMVC / SpringBoot

### 4.1 Spring 核心

#### 1. IoC 和 AOP 的理解？

**IoC（控制反转）**：
- 将对象的创建权交给 Spring 容器
- 降低耦合

**AOP（面向切面）**：
- 将横切关注点（日志、事务）抽离
- 实现无侵入式的增强

---

#### 2. Bean 生命周期？

```
1. 实例化（new）
2. 属性注入（populate）
3. 初始化：
   - BeanNameAware
   - BeanFactoryAware
   - BeanPostProcessor.postProcessBeforeInitialization
   - @PostConstruct
   - InitializingBean
   - BeanPostProcessor.postProcessAfterInitialization
4. 销毁：
   - @PreDestroy
   - DisposableBean.destroy()
```

---

#### 3. Spring 循环依赖？

**三级缓存**：
```java
singletonObjects = new ConcurrentHashMap<>();  // 一级：成品
earlySingletonObjects = new ConcurrentHashMap<>();  // 二级：半成品
singletonFactories = new ConcurrentHashMap<>();  // 三级：工厂
```

**解决流程**：
1. A 创建 → 三级缓存工厂
2. A 依赖 B → B 创建
3. B 依赖 A → 从三级缓存拿 A（提前暴露）
4. B 成品 → 一级缓存
5. A 完成 → 一级缓存

**无法解决**：
- 构造器注入
- prototype 作用域

---

#### 4. @Autowired 和 @Resource 的区别？

| 特性 | @Autowired | @Resource |
|------|------------|-----------|
| 来源 | Spring | JDK |
| 按类型匹配 | 是 | 默认按名称 |
| 按名称匹配 | @Qualifier | name 属性 |
| 找不到报错 | 是 | 否 |

---

#### 5. Spring 事务传播行为？

| 行为 | 说明 |
|------|------|
| REQUIRED | 有事务加入，无则新建 |
| REQUIRES_NEW | 总是新建事务 |
| NESTED | 嵌套事务（Savepoint） |
| SUPPORTS | 有则加入，无则非事务 |
| NOT_SUPPORTED | 挂起事务 |
| MANDATORY | 必须有事务 |
| NEVER | 必须无事务 |

---

#### 6. Spring 事务失效场景？

1. `private` 方法（代理问题）
2. 同类方法调用（this.xx()，无代理）
3. 异常被 catch
4. 数据库不支持事务（MyISAM）
5. 多数据源未指定事务管理器

---

### 4.2 SpringMVC

#### 7. SpringMVC 请求流程？

```
1. DispatcherServlet 接收请求
2. HandlerMapping 找处理器
3. HandlerAdapter 执行处理器
4. Controller 返回 ModelAndView
5. ViewResolver 解析视图
6. 渲染返回
```

---

#### 8. 拦截器和过滤器的区别？

| 特性 | 拦截器 | 过滤器 |
|------|--------|--------|
| 所属 | Spring | Servlet |
| 作用范围 | Controller | 任意 |
| 生命周期 | 初始化一次 | 每次请求 |
| 依赖 | Spring | Servlet |

---

### 4.3 SpringBoot

#### 9. SpringBoot 自动装配原理？

```java
@SpringBootApplication
  ↓
@EnableAutoConfiguration
  ↓
@Import(AutoConfigurationImportSelector.class)
  ↓
SpringFactoriesLoader 加载 META-INF/spring.factories
  ↓
@Conditional 条件装配
```

---

#### 10. Spring Boot 启动流程？

```java
SpringApplication.run()
  ↓
1. 创建 ApplicationContext
2. prepareContext() 预处理
3. refreshContext() 刷新容器
   - 加载 Bean
   - 启动内嵌 Tomcat
4. afterRefresh()
5. 发出 ApplicationStartedEvent
```

---

## 五、Spring Cloud 微服务

### 5.1 注册与发现

#### 1. Nacos 和 Eureka 的区别？

| 特性 | Nacos | Eureka |
|------|-------|--------|
| CAP | AP/CP 可切换 | AP |
| 配置管理 | 支持 | 不支持 |
| 命名空间 | 支持 | 不支持 |
| 保护机制 | 有 | 有 |
| 活跃度 | 活跃 | 停止维护 |

---

#### 2. Nacos AP/CP 模式？

- **AP 模式**：临时实例（心跳）
- **CP 模式**：永久实例（ Raft 共识）

```yaml
spring:
  cloud:
    nacos:
      discovery:
        ephemeral: false  # CP 模式
```

---

### 5.2 服务调用

#### 3. OpenFeign 工作原理？

```java
// 1. 注解标记接口
@FeignClient(name = "service-provider")
public interface UserService {
    @GetMapping("/user/{id}")
    User getUser(@PathVariable("id") Long id);
}

// 2. 动态代理生成实现
// 3. LoadBalancer 负载均衡
// 4. HTTP 客户端执行请求
```

---

### 5.3 流量控制

#### 4. Sentinel 限流算法？

| 算法 | 特点 |
|------|------|
| 直接拒绝 | 超出阈值直接拒绝 |
| 排队等待 | 匀速排队 |
| 滑动窗口 | 统计时间窗口 |
| 令牌桶 | 允许突发 |
| 漏桶 | 匀速处理 |

---

#### 5. 熔断器状态转换？

```
CLOSED（正常） → OPEN（熔断） → HALF_OPEN（半开）
```

- **CLOSED**：正常open
- **OPEN**：熔断，所有请求拒绝
- **HALF_OPEN**：尝试恢复

---

### 5.4 网关

#### 6. Gateway 工作原理？

```yaml
routes:
  - id: user-service
    uri: lb://user-service
    predicates:
      - Path=/user/**
    filters:
      - StripPrefix=1
```

**核心三要素**：
- Route：路由
- Predicate：断言
- Filter：过滤器

---

### 5.5 配置中心

#### 7. Nacos 配置动态刷新？

- **长轮询**：30秒轮询
- **MD5 对比**：配置没变不推送

```java
@RefreshScope  // 动态刷新
@RestController
public class ConfigController {
    @Value("${config.name}")
    private String name;
}
```

---

### 5.6 分布式事务

#### 8. Seata 事务模式？

| 模式 | 说明 | 适用场景 |
|------|------|----------|
| AT | 自动补偿 | 常规业务 |
| TCC | 手动补偿 | 性能要求高 |
| SAGA | 编排式 | 长流程 |
| XA | 两阶段提交 | 强一致性 |

---

## 六、MySQL 与数据库调优

### 6.1 基础知识

#### 1. InnoDB 和 MyISAM 的区别？

| 特性 | InnoDB | MyISAM |
|------|--------|--------|
| 事务 | 支持 | 不支持 |
| 行锁 | 支持 | 表锁 |
| 外键 | 支持 | 不支持 |
| 崩溃恢复 | 支持 | 不支持 |
| 全文索引 | 5.6+ 支持 | 原生支持 |

---

#### 2. 事务四大特性？

- **A**tomic：原子性
- **C**onsistency：一致性
- **I**solation：隔离性
- **D**urability：持久性

---

#### 3. 事务隔离级别？

| 级别 | 脏读 | 不可重复读 | 幻读 |
|------|------|------------|------|
| READ UNCOMMITTED | ✓ | ✓ | ✓ |
| READ COMMITTED | ✗ | ✓ | ✓ |
| REPEATABLE READ (默认) | ✗ | ✗ | ✓ |
| SERIALIZABLE | ✗ | ✗ | ✗ |

---

### 6.2 索引

#### 4. B+Tree 和 B-Tree 的区别？

| 特性 | B-Tree | B+Tree |
|------|--------|--------|
| 数据 | 节点存储 | 仅叶子节点存储 |
| 范围查询 | 需中序遍历 | 叶子节点链表 |
| IO次数 | 较多 | 较少 |

---

#### 5. 索引失效场景？

1. 左模糊查询：`%xxx`
2. 函数操作：`YEAR(create_time)`
3. 类型转换：`id = '123'`
4. OR 连接：一边无索引
5. 最左前缀不满足

---

### 6.3 锁机制

#### 6. MySQL 锁类型？

| 分类 | 锁 |
|------|-----|
| 粒度 | 表锁、行锁 |
| 模式 | 共享锁、排他锁 |
| 意图 | 意向锁 |
| 算法 | 间隙锁、临键锁 |

---

#### 7. 什么是临键锁？

记录锁 + 间隙锁的组合，锁定一个范围

**作用**：解决幻读（RR 级别）

---

### 6.4 日志与主从

#### 8. undo log、redo log、binlog？

| 日志 | 作用 | 存储 |
|------|------|------|
| undo | 回滚 | 系统表空间 |
| redo | 恢复已提交事务 | ib_logfile |
| binlog | 主从复制 | binlog 文件 |

---

#### 9. MySQL 两阶段提交？

```
1. 写 redo log（prepare）
2. 写 binlog
3. 写 redo log（commit）
```

保证 binlog 和 redo log 一致性

---

## 七、Redis 缓存与高可用

### 7.1 数据类型

#### 1. Redis 五种基本数据类型？

| 类型 | 底层 | 使用场景 |
|------|------|----------|
| String | SDS | 缓存、计数器 |
| List | QuickList | 消息队列、列表 |
| Hash | ZipList + HT | 对象 |
| Set | IntSet + HT | 去重、标签 |
| ZSet | ZipList + Skiplist | 排行榜 |

---

### 7.2 持久化

#### 2. RDB 和 AOF 的区别？

| 特性 | RDB | AOF |
|------|-----|-----|
| 方式 | 快照 | 命令 |
| 文件大小 | 小 | 大 |
| 恢复速度 | 快 | 慢 |
| 安全性 | 可能丢数据 | 可配置 |
| 性能 | Fork 子进程 | 追加 |

**推荐**：混合使用（RDB + AOF）

---

### 7.3 缓存问题

#### 3. 缓存穿透、击穿、雪崩？

| 问题 | 原因 | 解决 |
|------|------|------|
| 穿透 | 查询不存在数据 | 布隆过滤器、缓存空值 |
| 击穿 | 热点 key 过期 | 互斥锁、永不过期 |
| 雪崩 | 大量 key 同时过期 | 随机 TTL、集群 |

---

#### 4. 缓存更新策略？

| 策略 | 说明 |
|------|------|
| Cache Aside | 应用更新缓存（常用） |
| Read Through | 缓存加载数据 |
| Write Through | 缓存更新数据库 |
| Write Behind | 缓存异步写数据库 |

---

### 7.4 分布式锁

#### 5. Redis 分布式锁实现？

```java
// SET NX + 过期时间
String result = jedis.set("lock_key", "value", 
    "NX", "PX", 30000);

if ("OK".equals(result)) {
    try {
        // 业务逻辑
    } finally {
        jedis.del("lock_key");
    }
}
```

**问题**：
- 过期时间设置
- 锁续期（Watchdog）
- RedLock 可靠性

---

### 7.5 集群

#### 6. Redis Cluster 原理？

- **槽位**：16384 个槽
- **定位**：`CRC16(key) % 16384`
- **主从**：每个主节点可配置从节点
- **故障转移**：主从切换

---

## 八、MongoDB

### 1. MongoDB 和 MySQL 对比？

| MySQL | MongoDB |
|-------|---------|
| Table | Collection |
| Row | Document |
| Column | Field |
| JOIN | $lookup |

**适用场景**：
- 灵活 Schema
- 海量数据
- 文档存储

---

## 九、RocketMQ

### 1. RocketMQ 架构？

```
NameServer（注册中心）
    ↑
Producer → Broker → Consumer
```

**消息存储**：
- CommitLog：消息本体
- ConsumeQueue：消费队列
- IndexFile：索引

---

### 2. 消息顺序？

**全局有序**：一个队列
**局部有序**：同一订单相关放同一队列

```java
// MessageQueueSelector
producer.send(msg, (mqs, msg, arg) -> {
    String orderId = arg;
    int index = orderId.hashCode() % mqs.size();
    return mqs.get(index);
}, orderId);
```

---

### 3. 消息幂等？

**原因**：消费端重复消费

**解决**：
- 业务唯一键
- 去重表
- Redis 记录消费状态

---

## 十、分布式系统与架构设计

### 1. CAP 定理？

- **C**onsistency：一致性
- **A**vailability：可用性
- **P**artition tolerance：分区容错

**三者不可兼得**：P 必须满足，只能选 C 或 A

**常见选择**：
- CP：ZooKeeper、etcd
- AP：Eureka、Nacos

---

### 2. BASE 理论？

- **B**asically **A**vailable：基本可用
- **S**oft State：软状态
- **E**ventually Consistent：最终一致

---

### 3. 分布式 ID 方案？

| 方案 | 优点 | 缺点 |
|------|------|------|
| 数据库自增 | 简单 | 分库分表不行 |
| UUID | 分布式 | 无序、过长 |
| 雪花算法 | 有序、高效 | 时钟回拨 |
| Redis INCR | 简单 | 依赖 Redis |

---

### 4. 限流算法？

| 算法 | 特点 |
|------|------|
| 固定窗口 | 简单、临界突增 |
| 滑动窗口 | 精确 |
| 令牌桶 | 允许突发 |
| 漏桶 | 匀速 |

---

### 5. 秒杀系统设计？

1. **限流**：Sentinel/Gateway
2. **削峰**：MQ 消息队列
3. **库存扣减**：Redis 预减
4. **防超卖**：乐观锁
5. **异步下单**：MQ 持久化

---

## 十一、安全开发

### 1. SQL 注入？

**防御**：
- 预编译（PreparedStatement）
- 参数绑定
- 白名单过滤

---

### 2. XSS 攻击？

| 类型 | 特点 |
|------|------|
| 存储型 | 持久化 |
| 反射型 | URL 参数 |
| DOM 型 | 前端执行 |

**防御**：
- 转义
- CSP
- HttpOnly Cookie

---

### 3. CSRF 攻击？

**防御**：
- CSRF Token
- SameSite Cookie
- 双重提交

---

### 4. JWT 结构？

```
Header.Payload.Signature

Header: {"alg": "HS256", "typ": "JWT"}
Payload: {"sub": "123", "exp": "..."}
Signature: HMACSHA256(base64UrlEncode(header) + "." + base64UrlEncode(payload), secret)
```

---

## 十二、项目实战与场景题

### 12.1 信工所终端检查工具

> **项目简介**：面向企业的终端安全检查工具，支持客户端数据上报和服务端任务下发

#### 1. 微服务架构下双向交互设计？

**数据流向**：
```
客户端 → 上报检查结果 → 服务端（MongoDB 存储）
服务端 → 下发检查任务 → 客户端（MQ Tag 路由）
```

**核心交互**：
- 客户端主动上报：终端检查完成后上报结果
- 服务端任务下发：通过 RocketMQ 消息推送

---

#### 2. MongoDB 数据模型设计？

**挑战**：不同类型终端检查结果结构不同

**解决方案**：
- 利用 MongoDB 灵活 Schema
- 嵌套文档存储各类检查项
- 统一父类 + 差异化子类

```json
{
  "_id": "xxx",
  "terminalId": "T001",
  "checkTime": "2024-01-01",
  "checkItems": {
    "security": { "firewall": true, "antivirus": true },
    "software": { "installed": [...], "forbidden": [...] },
    "network": { "proxy": {...} }
  }
}
```

---

#### 3. 布隆过滤器实现？

```java
// Guava BloomFilter
BloomFilter<String> filter = BloomFilter.create(
    Funnels.stringFunnel(Charset.defaultCharset()),
    1000000,  // 预期插入数量
    0.01      // 误判率
);

// 添加
filter.put(terminalId);

// 检查
if (filter.mightContain(terminalId)) {
    // 可能存在，继续查询
}
```

**误判率计算**：`m = -n * ln(p) / (ln(2)^2)`

---

#### 4. Redis 分布式锁应用？

```java
RLock lock = redissonClient.getLock("terminal:check:" + terminalId);
try {
    boolean acquired = lock.tryLock(10, 30, TimeUnit.SECONDS);
    if (acquired) {
        // 执行检查结果上报
        saveCheckResult(result);
    }
} finally {
    if (lock.isHeldByCurrentThread()) {
        lock.unlock();
    }
}
```

---

#### 5. RocketMQ Tag 路由？

```java
// 生产者：按 Tag 发送
SendResult result = producer.send(
    msg,
    new MessageQueueSelector() {
        @Override
        public MessageQueue select(List<MessageQueue> mqs, Message msg, Object arg) {
            return mqs.get(0);
        }
    },
    "TASK_TYPE_CHECK",  // Tag: 检查任务
    3000
);

// 消费者：按 Tag 订阅
consumer.subscribe("TOPIC_TASK", "TASK_TYPE_CHECK");
```

---

#### 6. Seata 分布式事务？

**场景**：检查结果上报 + 状态更新

```java
@GlobalTransactional
public void reportCheckResult(CheckResult result) {
    // 1. 保存检查结果
    checkResultDao.insert(result);
    
    // 2. 更新终端状态
    terminalService.updateStatus(result.getTerminalId());
    
    // 3. 记录审计日志
    auditService.log(result);
}
```

---

#### 7. Sentinel 熔断降级？

```java
@SentinelResource(value = "checkAPI", 
    fallback = "checkFallback",
    blockHandler = "checkBlockHandler")
public CheckResult check(CheckRequest request) {
    return remoteService.check(request);
}

public CheckResult checkFallback(CheckRequest request) {
    // 降级返回
    return CheckResult.defaultResult();
}
```

---

#### 8. 敏感词检测优化？

**方案**：`Aho-Corasick` + `ANSJ` 分词

```java
// 1. ANSJ 中文分词
List<Term> terms = NlpAnalysis.parse(text).getTerms();

// 2. AC 自动机匹配
ACAutomaton<String> automaton = new ACAutomaton<>(sensitiveWords);
for (Term term : terms) {
    if (automaton.match(term.getName())) {
        // 命中敏感词
    }
}
```

---

### 12.2 数据库内容检查工具

> **项目简介**：支持 20+ 种数据库的统一检查工具

#### 1. 项目管理经验？

- **WBS 分解**：将项目拆分为可执行的任务
- **风险识别**：技术难点、人员流动、时间评估
- **应对策略**：预留缓冲、并行推进

---

#### 2. 多数据库适配设计？

**适配器模式 + 策略模式**：

```java
// 抽象适配器
public interface DatabaseAdapter {
    Connection connect(ConnectionInfo info);
    ResultSet query(Connection conn, String sql);
    void close(Connection conn);
}

// MySQL 适配器
public class MySqlAdapter implements DatabaseAdapter {
    @Override
    public Connection connect(ConnectionInfo info) {
        return DriverManager.getConnection(
            "jdbc:mysql://" + info.getHost() + ":" + info.getPort(),
            info.getUser(), info.getPassword()
        );
    }
}
```

---

#### 3. Quartz 集群防重复？

```java
// 数据库锁
SELECT * FROM QRTZ_LOCKS WHERE LOCK_NAME = 'TRIGGER_ACCESS' FOR UPDATE;
```

---

### 12.3 车企应用集成平台

> **项目简介**：单体应用迁移到微服务架构

#### 1. 微服务改造挑战？

- **数据一致性**：分布式事务
- **服务边界**：领域划分
- **事务拆分**：Saga 模式

---

#### 2. 数据迁移方案？

1. **双写**：新系统写入时同步写旧系统
2. **增量同步**：Canal 监听 binlog
3. **校验**：数据对比

---

#### 3. CI/CD 流程？

```
代码提交 → GitLab
    ↓
Jenkins Pipeline
    ↓
1. Maven 构建
2. 单元测试
3. SonarQube 扫描
4. Docker 镜像构建
5. 镜像推送 Harbor
6. K8s 部署（灰度）
    ↓
钉钉通知
```

---

### 12.4 通用场景题

#### 1. 接口突然变慢排查？

```
1. 查看日志：异常、慢请求
2. 查看监控：CPU、内存、GC
3. 链路追踪：SkyWalking 定位
4. 数据库：慢查询、连接池
5. 缓存：命中率、热点
```

---

#### 2. Redis 挂了如何降级？

1. 熔断：快速失败
2. 降级：返回默认值
3. 本地缓存：guava/cahce
4. 异步写入：恢复后补偿

---

#### 3. 消息积压处理？

1. 扩容消费者
2. 提高并发消费
3. 批量消费
4. 跳过不重要消息

---

## 十三、设计模式

### 1. 单例模式？

```java
// 双重检查锁
public class Singleton {
    private static volatile Singleton instance;
    
    private Singleton() {}
    
    public static Singleton getInstance() {
        if (instance == null) {
            synchronized (Singleton.class) {
                if (instance == null) {
                    instance = new Singleton();
                }
            }
        }
        return instance;
    }
}
```

**volatile 作用**：防止指令重排序

---

### 2. 策略模式消除 if-else？

```java
// 支付策略
public interface PayStrategy {
    PayResult pay(Order order);
}

@Component
public class WechatPayStrategy implements PayStrategy {}
@Component
public class AlipayStrategy implements PayStrategy {}

// 使用
@Service
public class PayService {
    @Autowired
    private Map<String, PayStrategy> strategies;
    
    public PayResult pay(String type, Order order) {
        PayStrategy strategy = strategies.get(type);
        return strategy.pay(order);
    }
}
```

---

### 3. 装饰器模式？

```java
// BufferedInputStream 装饰 FileInputStream
InputStream in = new BufferedInputStream(
    new FileInputStream("file.txt")
);
```

---

## 十四、Go 语言

### 1. Go 和 Java 的区别？

| 特性 | Go | Java |
|------|-----|------|
| 编译 | 编译型 | 解释型/编译型 |
| GC | 三色标记 | 分代收集 |
| 并发 | goroutine | Thread |
| 指针 | 有 | 无 |
| 接口 | 隐式实现 | 显式实现 |

---

### 2. goroutine vs Thread？

- goroutine：轻量级（2KB栈），可创建百万级
- Thread：1MB栈，创建成本高

---

### 3. Channel 有缓冲 vs 无缓冲？

- **无缓冲**：同步阻塞
- **有缓冲**：异步，不阻塞

```go
ch := make(chan int)       // 无缓冲
ch := make(chan int, 10)    // 有缓冲，容量 10
```

---

## 十五、DevOps

### 1. Docker 常用命令？

```bash
# 构建镜像
docker build -t myapp:1.0 .

# 运行容器
docker run -d -p 8080:8080 myapp:1.0

# 查看日志
docker logs -f container_id

# 进入容器
docker exec -it container_id bash
```

---

### 2. Dockerfile 优化？

```dockerfile
# 多阶段构建
FROM maven:3.8 AS builder
COPY . /app
RUN mvn package -DskipTests

FROM openjdk:11-jre
COPY --from=builder /app/target/app.jar /app.jar
ENTRYPOINT ["java", "-jar", "/app.jar"]
```

---

## 十六、网络协议

### 1. TCP 三次握手？

```
客户端 → SYN → 服务器
客户端 ← SYN+ACK ← 服务器
客户端 → ACK → 服务器
```

---

### 2. TCP 四次挥手？

```
客户端 → FIN → 服务器
客户端 ← ACK ← 服务器
[客户端等待]
客户端 ← FIN ← 服务器
客户端 → ACK → 服务器
```

---

### 3. HTTP 状态码？

| 状态码 | 含义 |
|--------|------|
| 200 | 成功 |
| 301 | 永久重定向 |
| 302 | 临时重定向 |
| 304 | 缓存 |
| 400 | 请求错误 |
| 401 | 未授权 |
| 403 | 禁止 |
| 404 | 未找到 |
| 500 | 服务器错误 |
| 502 | 网关错误 |
| 503 | 服务不可用 |

---

## 十七、MyBatis / MyBatis-Plus

### 1. #{} 和 ${} 的区别？

- `#{}`：预编译（PreparedStatement），防止 SQL 注入
- `${}`：字符串替换，有 SQL 注入风险

**使用场景**：
- `#{}`：普通参数
- `${}`：动态表名、排序字段

---

### 2. 一级缓存和二级缓存？

- **一级缓存**：SqlSession 级别，默认开启
- **二级缓存**：Mapper 级别，需要手动开启

---

## 十八、PostgreSQL

### 1. PostgreSQL vs MySQL？

| 特性 | PostgreSQL | MySQL |
|------|------------|-------|
| 复杂查询 | 强 | 一般 |
| JSON 支持 | JSONB（高性能） | JSON |
| 窗口函数 | 原生支持 | 8.0+ |
| 并发控制 | MVCC | MVCC |

---

## 十九、Elasticsearch

### 1. ES 核心概念？

- **Index**：索引（类似数据库）
- **Document**：文档（类似行）
- **Type**：类型（7.x 已废弃）
- **Shard**：分片
- **Replica**：副本

---

### 2. 倒排索引原理？

```
正排：文档 → 词项
倒排：词项 → 文档列表
```

**优势**：适合全文检索

---

### 3. ES 查询类型？

| 类型 | 用途 |
|------|------|
| term | 精确匹配 |
| match | 全文匹配 |
| range | 范围查询 |
| bool | 组合查询 |

---

## 二十、数据结构与算法

### 1. 时间复杂度排序？

```
O(1) < O(logn) < O(n) < O(nlogn) < O(n²) < O(2ⁿ) < O(n!)
```

---

### 2. 数组 vs 链表？

| 特性 | 数组 | 链表 |
|------|------|------|
| 访问 | O(1) | O(n) |
| 插入/删除 | O(n) | O(1) |
| 内存 | 连续 | 分散 |
| 空间 | 小 | 大（指针） |

---

### 3. HashMap 查找 O(1)？

- 数组：O(1) 定位
- 链表/红黑树：O(n)/O(logn) 查找

**均摊**：O(1)

---

### 4. Top K 问题？

**堆**方法：
```java
// 求 Top K 大：使用最小堆
PriorityQueue<Integer> minHeap = new PriorityQueue<>(k);
for (int num : nums) {
    minHeap.offer(num);
    if (minHeap.size() > k) {
        minHeap.poll();
    }
}
```

---

### 5. 排序算法对比？

| 算法 | 时间 | 空间 | 稳定 |
|------|------|------|------|
| 冒泡 | O(n²) | O(1) | ✓ |
| 插入 | O(n²) | O(1) | ✓ |
| 归并 | O(nlogn) | O(n) | ✓ |
| 快速 | O(nlogn) | O(logn) | ✗ |
| 堆 | O(nlogn) | O(1) | ✗ |

---

## 二十一、综合软实力

### 1. 项目介绍技巧（STAR法则）？

- **S**ituation：项目背景
- **T**ask：你的职责
- **A**ction：具体行动
- **R**esult：最终成果

---

### 2. 技术成长最快阶段？

结合经历：
- 独立负责项目
- 解决生产问题
- 性能优化经历
- 架构改造经验

---

### 3. 职业规划？

- 1-2年：深耕技术，成为高级工程师
- 3-5年：技术专家或技术管理

---

### 4. 为什么从北京回沈阳？

- 离家近
- 沈阳 IT 发展
- 生活成本
- 工作生活平衡

---

## 📌 附录：高频手写题

```
1. 手写单例模式（DCL）
2. 手写 LRU 缓存
3. 手写生产者-消费者
4. 手写线程池
5. 手写快速排序
6. 手写反转链表
7. 手写二叉树遍历
8. 手写 HashMap
9. 手写 RPC 框架
10. 手写布隆过滤器
11. 手写两个栈实现队列
12. 手写归并排序
13. 手写二分查找
14. 手写判断链表有环
15. 手写分布式锁
```

---

## 📝 使用建议

- 按章节顺序复习，由浅入深
- 项目经验结合 STAR 法则
- 手写题实际练习
- 关注"原理 → 使用场景 → 踩坑"三个维度

---

*祝面试顺利，offer 多多！🎯*
