Naming
======
`naming` is a generic naming convention library.

```python
import naming as n

# setup a new profile
p = n.new_profile("test")

n.new_token("l", "L")
n.new_token("r", "R")
n.new_token("m", "M")
n.new_token("g", "GEO")
n.new_token("a", "ANIM")

f = p.add_field("side")
f.append_token("l")
f.append_token("r")
f.append_token("m")
f.set_default("m")

p.add_field("name")

f = p.add_field("type")
f.append_token("g")
f.append_token("a")
f.set_default("g")

# use naming to solve your names
print(n.solve("test"))
# M_test_GEO

print(n.solve("test", "a"))
# M_test_ANIM
```

## Notes

###  Good
- setup.py
- tests

### Bad
- unittest
- pyproject
- No GHA
- 