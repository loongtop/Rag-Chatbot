---
status: draft
owner: tester
function: {function_name}
module: {module_name}
generated_from: {design_md_path}
language_profile: python
---

# Test Suite: {function_name}

> 自动生成的测试文件 - 基于 design.md 中的测试用例
>
> **注**：此模板适用于 `language_profile: python`。其他语言请参考对应的测试框架（JUnit/GTest 等）自行调整。

## Import and Setup

```python
import pytest
from {module_path} import {function_name}
from unittest.mock import Mock, patch

# Test fixtures
@pytest.fixture
def sample_data():
    """提供测试数据"""
    return {
        "valid_input": {...},
        "invalid_input": {...}
    }
```

---

## 功能测试 (Functional Tests)

### Test 1: {测试名称} - 正常流程

```python
def test_{function_name}_normal_case_1(sample_data):
    """
    测试正常使用场景
    
    Given: {给定条件}
    When: {执行操作}
    Then: {预期结果}
    """
    # Arrange
    input_data = sample_data["valid_input"]
    
    # Act
    result = {function_name}(input_data)
    
    # Assert
    assert result == {expected_value}
    assert isinstance(result, {expected_type})
```

### Test 2: {测试名称} - 另一个正常场景

```python
def test_{function_name}_normal_case_2():
    """测试另一个正常场景"""
    # Arrange
    {setup_code}
    
    # Act
    result = {function_name}({input})
    
    # Assert
    assert result == {expected}
```

---

## 边界测试 (Boundary Tests)

### Test 3: 空值处理

```python
def test_{function_name}_empty_input():
    """测试空值输入"""
    # Test empty string
    result = {function_name}("")
    assert result == {expected_for_empty}
    
    # Test empty list
    result = {function_name}([])
    assert result == {expected_for_empty_list}
```

### Test 4: None 值处理

```python
def test_{function_name}_none_input():
    """测试 None 输入"""
    # Option 1: Returns default value
    result = {function_name}(None)
    assert result == {default_value}
    
    # Option 2: Raises exception
    with pytest.raises(ValueError, match="input cannot be None"):
        {function_name}(None)
```

### Test 5: 最大值/最小值

```python
def test_{function_name}_boundary_values():
    """测试边界值"""
    # Minimum value
    result = {function_name}(0)
    assert result == {expected_min}
    
    # Maximum value
    result = {function_name}(999999)
    assert result == {expected_max}
```

### Test 6: 超长输入

```python
def test_{function_name}_large_input():
    """测试超长字符串/列表"""
    long_string = "x" * 10000
    result = {function_name}(long_string)
    
    # Verify handling (truncate, reject, or process)
    assert len(result) <= {max_length}
```

---

## 异常测试 (Exception Tests)

### Test 7: 错误类型输入

```python
def test_{function_name}_wrong_type():
    """测试错误数据类型"""
    with pytest.raises(TypeError, match="expected str"):
        {function_name}(12345)  # Should be string
    
    with pytest.raises(TypeError, match="expected int"):
        {function_name}("not a number")  # Should be int
```

### Test 8: 业务逻辑异常

```python
def test_{function_name}_business_logic_failure():
    """测试业务逻辑失败场景"""
    # Example: User not found
    result = {function_name}("nonexistent_user")
    assert result is False
    
    # Example: Invalid credentials
    with pytest.raises(AuthenticationError):
        {function_name}("user", "wrong_password")
```

### Test 9: 依赖失败

```python
@patch('{module_path}.database')
def test_{function_name}_dependency_failure(mock_db):
    """测试外部依赖失败"""
    # Mock database connection failure
    mock_db.connect.side_effect = ConnectionError("DB unavailable")
    
    with pytest.raises(DatabaseError):
        {function_name}({input})
```

---

## 性能测试 (Performance Tests)

### Test 10: 响应时间

```python
def test_{function_name}_performance():
    """验证响应时间 < {max_ms}ms"""
    import time
    
    start = time.time()
    result = {function_name}({normal_input})
    duration = time.time() - start
    
    assert duration < {max_seconds}  # e.g., 0.1 for 100ms
    assert result == {expected}  # Still returns correct result
```

### Test 11: 内存使用

```python
def test_{function_name}_memory_usage():
    """验证内存使用合理"""
    import tracemalloc
    
    tracemalloc.start()
    result = {function_name}({large_input})
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    # Verify memory usage < {max_mb} MB
    assert peak < {max_bytes}  # e.g., 10 * 1024 * 1024 for 10MB
```

---

## 安全测试 (Security Tests) - 如适用

### Test 12: SQL 注入防护

```python
def test_{function_name}_sql_injection_protection():
    """验证 SQL 注入防护"""
    malicious_input = "admin' OR '1'='1"
    
    # Should safely handle or reject
    result = {function_name}(malicious_input)
    assert result is False  # or safely escaped
```

### Test 13: XSS 防护

```python
def test_{function_name}_xss_protection():
    """验证 XSS 防护"""
    malicious_script = "<script>alert('xss')</script>"
    
    result = {function_name}(malicious_script)
    
    # Should be escaped
    assert "&lt;script&gt;" in result
    assert "<script>" not in result
```

---

## 集成测试 (Integration Tests) - 如适用

### Test 14: 数据库集成

```python
@pytest.mark.integration
def test_{function_name}_with_database(db_session):
    """测试数据库集成"""
    # Setup
    test_data = db_session.create({test_record})
    
    # Test
    result = {function_name}(test_data.id)
    
    # Assert
    assert result.id == test_data.id
    
    # Cleanup
    db_session.delete(test_data)
```

---

## Test Coverage Summary

```
功能测试:    2 tests  ✓
边界测试:    4 tests  ✓
异常测试:    3 tests  ✓
性能测试:    2 tests  ✓
安全测试:    2 tests  ✓ (if applicable)
集成测试:    1 test   ✓ (if applicable)
------------------------------------
总计:        14+ tests
```

## Run Tests

```bash
# Run all tests for this function
pytest tests/test_{module_name}.py::Test{FunctionName} -v

# Run with coverage
pytest tests/test_{module_name}.py::Test{FunctionName} --cov={module_path}

# Run only functional tests
pytest tests/test_{module_name}.py::Test{FunctionName} -m functional

# Run only performance tests
pytest tests/test_{module_name}.py::Test{FunctionName} -m performance
```
