## 一、Java 基础与核心（扩展补充）

### 1.6 Java IO / NIO / AIO

1. Java IO 体系的核心类有哪些？字节流和字符流的根类分别是什么？
2. `InputStream` 和 `Reader` 的区别是什么？什么场景用字节流，什么场景用字符流？
3. `BufferedReader` / `BufferedWriter` 为什么能提升 IO 性能？缓冲区的工作原理是什么？
4. `InputStreamReader` 和 `OutputStreamWriter` 的作用是什么？它们是什么设计模式的体现？
5. `FileInputStream` 直接读文件和 `BufferedInputStream` 包装后读文件的性能差异有多大？为什么？
6. BIO（Blocking IO）、NIO（Non-blocking IO）、AIO（Asynchronous IO）的区别是什么？
7. Java NIO 的三个核心组件是什么？（Channel、Buffer、Selector）
8. `ByteBuffer` 中 `position`、`limit`、`capacity` 的含义分别是什么？`flip()` 做了什么？
9. `Selector` 的工作原理是什么？为什么它能实现单线程处理多个连接？
10. NIO 中的 `SelectionKey` 有哪几种事件类型？（`OP_ACCEPT`、`OP_CONNECT`、`OP_READ`、`OP_WRITE`）
11. 什么是零拷贝（Zero-Copy）？`FileChannel.transferTo()` 是如何实现零拷贝的？
12. `DirectByteBuffer`（堆外内存）和 `HeapByteBuffer` 的区别？堆外内存的优缺点？
13. Netty 是基于 NIO 的，它解决了原生 NIO 的哪些痛点？
14. `Files`、`Paths`、`Path` 是 Java NIO.2 的 API，和传统 `File` 类相比有哪些优势？
15. `WatchService` 是什么？如何用它监听文件系统变化？

### 1.7 Java 反射与动态代理

16. 什么是 Java 反射？反射的核心类有哪些？（`Class`、`Method`、`Field`、`Constructor`）
17. 获取 `Class` 对象的三种方式是什么？它们有什么区别？
18. 反射调用方法时，`method.invoke()` 的参数和返回值处理有什么注意点？
19. 反射的性能为什么比直接调用慢？如何优化（`setAccessible(true)`、方法句柄 `MethodHandle`）？
20. `getDeclaredMethods()` 和 `getMethods()` 的区别？`getDeclaredField()` 和 `getField()` 的区别？
21. JDK 动态代理的核心原理是什么？`Proxy.newProxyInstance()` 需要哪些参数？
22. JDK 动态代理为什么只能代理接口，不能代理类？
23. CGLIB 动态代理的原理是什么？它是如何在运行时生成子类的？
24. `InvocationHandler` 的 `invoke()` 方法三个参数分别是什么含义？
25. 什么是字节码增强？ASM、Javassist、ByteBuddy 分别是什么？SkyWalking Agent 用的是哪个？
26. Java `MethodHandle`（方法句柄）是什么？它相比反射有哪些优势？

### 1.8 Java 序列化与反序列化

27. Java 序列化的作用是什么？如何让一个类可序列化？
28. `serialVersionUID` 的作用是什么？不显式声明会有什么问题？
29. `transient` 关键字的作用是什么？被 `transient` 修饰的字段在序列化时如何处理？
30. `Externalizable` 和 `Serializable` 的区别是什么？
31. Java 原生序列化的缺点有哪些？（性能差、不跨语言、序列化后体积大、安全漏洞）
32. 常见的序列化框架有哪些？（JSON: Jackson/Gson/FastJSON2，二进制: Protobuf/Kryo/Hessian）各自的优缺点？
33. `FastJSON` 的反序列化漏洞是什么？如何防范？为什么推荐用 `FastJSON2` 替代？
34. Protobuf 的序列化原理是什么？为什么它比 JSON 体积小、速度快？
35. 在微服务 RPC 调用中，选择什么序列化协议？考虑哪些因素？

### 1.9 Java 新特性深入（Java 11 ~ Java 21）

36. Java 11 引入的 `var` 关键字（局部变量类型推断）有哪些限制？
37. Java 14 的 `switch` 表达式（`switch` expression）和传统 `switch` 语句的区别？
38. Java 15 的文本块（Text Blocks）解决了什么问题？
39. Java 16 的 `instanceof` 模式匹配是什么？
40. Java 17 的密封类（`sealed class`）的使用场景是什么？
41. Java 19/21 引入的虚拟线程（Virtual Threads / Project Loom）是什么？它如何解决传统线程的问题？
42. Java 21 的结构化并发（Structured Concurrency）是什么概念？
