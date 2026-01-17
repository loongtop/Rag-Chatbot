# Test Generate Module

> 内部模块 - 由 tester-agent 调用，用户不可直接触发

## 职责

根据测试计划或 Spec 生成测试代码。

## 输入（按优先级）

1. `docs/testing/test_plan_*.md`（由 test-design 模块生成）
2. `specs/SPEC-*.md`（leaf=true）的 Acceptance Tests
3. `design.md` 的 Test Spec

## 输出

- `apps/{component}/tests/**/*.py`（或对应语言的测试文件）

## 执行逻辑

1. **读取测试规格**
   - 解析测试计划或 Spec
   - 提取测试用例列表

2. **读取源代码**
   - 读取对应的实现代码
   - 理解函数签名和接口

3. **生成测试代码**

   ```python
   # 功能测试
   def test_{function}_normal_case():
       """测试正常流程"""
       ...
   
   # 边界测试
   def test_{function}_empty_input():
       """测试空输入"""
       ...
   
   # 异常测试
   def test_{function}_invalid_input():
       """测试无效输入"""
       ...
   
   # 性能测试
   def test_{function}_performance():
       """测试响应时间"""
       ...
   ```

4. **验证生成结果**
   - 确保覆盖所有测试用例
   - 确保断言包含说明

## 质量标准

| 类型 | 最少数量 |
|------|----------|
| 功能测试 | 2 |
| 边界测试 | 4 |
| 异常测试 | 3 |
| 性能测试 | 1 |
