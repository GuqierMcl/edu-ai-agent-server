#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
雪花ID生成器
@Project : AAServer 
@File    : snowflake.py
@IDE     : PyCharm 
@Author  : Guqier
@Date    : 2025/8/7 14:31 
@Version : 1.0
"""
import time
import threading

class Snowflake:
    """单机雪花算法生成器"""
    TWEPOCH = 1288834974657  # 基准时间戳
    WORKER_ID_BITS = 5
    DATACENTER_ID_BITS = 5
    SEQUENCE_BITS = 12
    MAX_WORKER_ID = (1 << WORKER_ID_BITS) - 1
    MAX_DATACENTER_ID = (1 << DATACENTER_ID_BITS) - 1
    SEQUENCE_MASK = (1 << SEQUENCE_BITS) - 1

    def __init__(self, datacenter_id=1, worker_id=1):
        if worker_id > self.MAX_WORKER_ID or datacenter_id > self.MAX_DATACENTER_ID:
            raise ValueError("worker_id 或 datacenter_id 超限")
        self.worker_id = worker_id
        self.datacenter_id = datacenter_id
        self.sequence = 0
        self.last_timestamp = -1
        self.lock = threading.Lock()

    def _now(self):
        return int(time.time() * 1000)

    def next_id(self):
        with self.lock:
            timestamp = self._now()
            if timestamp < self.last_timestamp:
                raise RuntimeError("时钟回拨")
            if timestamp == self.last_timestamp:
                self.sequence = (self.sequence + 1) & self.SEQUENCE_MASK
                if self.sequence == 0:
                    while timestamp <= self.last_timestamp:
                        timestamp = self._now()
            else:
                self.sequence = 0
            self.last_timestamp = timestamp
            return (
                ((timestamp - self.TWEPOCH) << (self.WORKER_ID_BITS + self.DATACENTER_ID_BITS + self.SEQUENCE_BITS)) |
                (self.datacenter_id << (self.WORKER_ID_BITS + self.SEQUENCE_BITS)) |
                (self.worker_id << self.SEQUENCE_BITS) |
                self.sequence
            )

# 单例
snowflake = Snowflake(datacenter_id=1, worker_id=1)

def next_id() -> int:
    return snowflake.next_id()