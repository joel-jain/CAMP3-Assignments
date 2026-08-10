
class Printer:
    def __init__(self, printer_name):
        self.printer_name = printer_name

    def print_document(self):
        print(f"Printing document on {self.printer_name}")


class Scanner:
    def __init__(self, scan_resolution):
        self.scan_resolution = scan_resolution

    def scan_document(self):
        print(f"Scanning at {self.scan_resolution} dpi")

class AllInOnePrinter(Printer, Scanner):
    def __init__(self, printer_name, scan_resolution):
        Printer.__init__(self, printer_name)
        Scanner.__init__(self, scan_resolution)

obj_printer = AllInOnePrinter("HP LaserJet", 600)

obj_printer.print_document()
obj_printer.scan_document()
