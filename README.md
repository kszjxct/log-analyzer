 日志分析工具

读取 .log 文件，统计 INFO / WARNING / ERROR 各级别数量，
并把错误明细导出为报告文件。

 用法

    python logtool.py

默认分析当前目录下的 sample.log，结果输出到 report.txt。

 输出示例

    总行数:50
    INFO:16
    WARNING:22
    ERROR:12

    ->共12条ERROR:
    ->2026-11-02 14:04:00[ERROR]用户登录成功

 说明

- 逐行读取，不一次性加载整个文件
- 从 [ERROR] 标签中精确提取级别，避免正文出现同名关键字被误判
- 使用 with open 保证文件正确关闭
