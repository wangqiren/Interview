## 网络协议基础（新增章节）

### HTTP 协议

1. HTTP/1.0、HTTP/1.1、HTTP/2、HTTP/3 的主要区别是什么？
2. HTTP/1.1 的 `keep-alive` 长连接是如何工作的？它解决了什么问题？
3. HTTP/2 的多路复用（Multiplexing）是什么？它是如何解决 HTTP/1.1 的队头阻塞问题的？
4. HTTP/2 的头部压缩（HPACK）原理是什么？
5. HTTP/3 为什么基于 QUIC 协议而不是 TCP？QUIC 解决了什么问题？
6. HTTP 请求报文和响应报文的结构分别是什么？
7. HTTP 常见状态码：`200`、`301`、`302`、`304`、`400`、`401`、`403`、`404`、`500`、`502`、`503` 各代表什么？
8. `GET` 和 `POST` 的区别是什么？从语义、幂等性、安全性角度分析。
9. `PUT`、`PATCH`、`DELETE` 的语义分别是什么？
10. HTTP 的 `Cookie` 和 `Session` 机制是如何工作的？
11. 什么是 `Content-Type`？`application/json`、`application/x-www-form-urlencoded`、`multipart/form-data` 的区别？
12. 什么是 CORS（跨域资源共享）？为什么会有跨域问题？预检请求（Preflight）是什么？
13. HTTP 缓存机制是什么？`Cache-Control`、`ETag`、`Last-Modified` 各有什么作用？
14. RESTful API 设计规范是什么？如何设计一套良好的 RESTful 接口？
15. 什么是 GraphQL？它和 REST 相比有哪些优缺点？

### TCP/IP 协议

16. TCP 和 UDP 的区别是什么？各自适合什么场景？
17. TCP 三次握手的过程是什么？为什么是三次而不是两次或四次？
18. TCP 四次挥手的过程是什么？为什么断开连接需要四次而不是三次？
19. `TIME_WAIT` 状态是什么？为什么需要等待 2MSL？
20. TCP 如何保证可靠传输？（序号/确认号、超时重传、滑动窗口、流量控制、拥塞控制）
21. TCP 的滑动窗口机制是什么？发送窗口和接收窗口有什么关系？
22. TCP 的拥塞控制算法有哪几个阶段？（慢启动、拥塞避免、快重传、快恢复）
23. 什么是 TCP 的粘包和拆包问题？如何解决？
24. `SYN Flood` 攻击的原理是什么？如何防御？
25. DNS 解析的完整流程是什么？（递归查询、迭代查询）
26. `127.0.0.1` 和 `localhost` 的区别？`0.0.0.0` 是什么意思？

### WebSocket

27. WebSocket 和 HTTP 的区别是什么？WebSocket 握手是如何进行的？
28. 什么场景下选择 WebSocket？（实时通信、消息推送、在线协作）
29. WebSocket 的心跳机制是如何实现的？为什么需要心跳？
30. Spring Boot 中如何集成 WebSocket？`@ServerEndpoint` 注解如何使用？
31. WebSocket 在集群环境下如何处理会话共享？（Redis pub/sub 方案）

---

## 持久层框架（新增章节）

### MyBatis 核心

1. MyBatis 和 Hibernate（JPA）的区别是什么？各自适合什么场景？
2. MyBatis 的核心组件有哪些？（`SqlSessionFactory`、`SqlSession`、`Mapper`、`Executor`）
3. MyBatis 的 `#{}` 和 `${}` 的区别是什么？为什么 `${}` 会有 SQL 注入风险？
4. MyBatis 的一级缓存和二级缓存是什么？各自的作用范围和失效条件？
5. MyBatis 的插件（Plugin / Interceptor）机制是什么？可以拦截哪些对象？
6. MyBatis 如何处理结果集映射（`ResultMap`）？嵌套查询和嵌套结果的区别？
7. MyBatis 中 `<if>`、`<choose>`、`<foreach>`、`<trim>` 等动态 SQL 标签的使用场景？
8. MyBatis 的 `Executor` 有哪几种类型？（`SimpleExecutor`、`ReuseExecutor`、`BatchExecutor`）
9. MyBatis 如何实现分页？物理分页和逻辑分页的区别？`PageHelper` 的原理是什么？
10. MyBatis 如何处理大字段（BLOB/CLOB）的延迟加载（Lazy Loading）？

### MyBatis-Plus

11. MyBatis-Plus 相比 MyBatis 额外提供了哪些功能？
12. `BaseMapper` 中内置了哪些 CRUD 方法？`IService` 层的作用是什么？
13. MyBatis-Plus 的 `QueryWrapper` 和 `LambdaQueryWrapper` 的区别？为什么推荐用 Lambda 方式？
14. MyBatis-Plus 的代码生成器（Generator）是如何工作的？
15. MyBatis-Plus 的乐观锁插件（`@Version`）如何实现乐观锁？
16. MyBatis-Plus 的逻辑删除（`@TableLogic`）是如何实现的？有哪些注意事项？
17. MyBatis-Plus 的自动填充功能（`@TableField(fill = ...)` + `MetaObjectHandler`）如何使用？
18. MyBatis-Plus 的多租户插件（`TenantLineInnerInterceptor`）原理是什么？
19. MyBatis-Plus 的分页插件（`PaginationInnerInterceptor`）和 `PageHelper` 的区别？

---

## PostgreSQL（新增章节）

1. PostgreSQL 和 MySQL 的主要区别是什么？什么场景下选择 PostgreSQL？
2. PostgreSQL 支持哪些 MySQL 没有的数据类型？（`JSONB`、数组类型、范围类型、UUID 等）
3. PostgreSQL 的 `JSONB` 和 `JSON` 类型的区别是什么？`JSONB` 有哪些优势？
4. PostgreSQL 的索引类型有哪些？（B-tree、Hash、GiST、GIN、BRIN）各自适合什么场景？
5. PostgreSQL 的 `EXPLAIN ANALYZE` 输出如何读懂？
6. PostgreSQL 的窗口函数（Window Function）是什么？`ROW_NUMBER()`、`RANK()`、`LAG()` 的使用场景？
7. PostgreSQL 的 CTE（公用表表达式，`WITH` 语句）是什么？和子查询相比有什么优势？
8. PostgreSQL 的继承（Table Inheritance）特性是什么？
9. PostgreSQL 的 MVCC 实现和 MySQL 的 MVCC 有什么不同？
10. 从 Oracle 迁移到 PostgreSQL，需要注意哪些兼容性问题？（语法差异、函数差异、序列 vs 自增）
11. `SERIAL` 和 `SEQUENCE` 的关系是什么？PostgreSQL 中自增主键如何实现？
12. PostgreSQL 的 `VACUUM` 和 `ANALYZE` 命令的作用是什么？为什么 PostgreSQL 需要 VACUUM？
13. PostgreSQL 的逻辑复制（Logical Replication）和流复制（Streaming Replication）的区别？

---

## Elasticsearch（新增章节）

> 简历中的数据库检查工具支持 Elasticsearch，面试中可能被问到

1. Elasticsearch 的核心概念有哪些？（Index、Document、Shard、Replica、Mapping）
2. ES 和关系型数据库的概念对比：Index vs Table，Document vs Row，Field vs Column？
3. 倒排索引（Inverted Index）的原理是什么？ES 为什么擅长全文检索？
4. ES 的分词器（Analyzer）是什么？有哪些常用的中文分词器？（IK Analyzer）
5. ES 的 `Mapping` 是什么？`dynamic mapping` 和 `explicit mapping` 的区别？
6. ES 查询中 `query context` 和 `filter context` 的区别？（相关性评分 vs 是/否过滤）
7. `term`、`match`、`match_phrase`、`multi_match` 查询的区别是什么？
8. ES 的聚合查询（Aggregation）有哪些类型？（`terms`、`date_histogram`、`avg`、`nested`）
9. ES 的写入流程是什么？数据写入后多久能被搜索到？（`refresh` 机制）
10. ES 的分布式架构：主分片（Primary Shard）和副本分片（Replica Shard）的作用？
11. ES 集群的健康状态：`green`、`yellow`、`red` 分别代表什么？
12. 如何优化 ES 的写入性能？（批量写入 `_bulk`、减少 `refresh` 频率、禁用副本后再开启）
13. 如何优化 ES 的查询性能？（使用 `filter` 而非 `query`、避免深翻页、使用 `search_after`）
14. ES 的深翻页问题如何解决？`from+size`、`scroll`、`search_after` 的区别？
15. ES 和数据库如何保证数据一致性？（双写方案、Canal 监听 binlog 同步方案）
