from ClassLibrary import DataCell as d
from ClassLibrary import ProcessManager as p
d1 = d.DataCell("Kiss Géza")
ProcessManager = p.ProcessManager()

print(d1.value)

ProcessManager.StartSession()