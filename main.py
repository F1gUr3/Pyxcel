from ClassLibrary import DataCell as d
from ClassLibrary import ProcessManager
d1 = d.DataCell("Kiss Géza")
ProcessManager = ProcessManager.ProcessManager()

print(d1.value)

ProcessManager.StartSession()