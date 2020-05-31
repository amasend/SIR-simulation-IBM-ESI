__all__ = [
    "HistogramTxt",
    "HistogramJSON",
    "HistogramXml"
]

from histogram_api import HistogramInterface
import json
import xml.etree.ElementTree as ET
import csv


class HistogramTxt(HistogramInterface):
    def read_data(self, file_path: str) -> str:
        extension = file_path[file_path.rfind("."):]

        if extension == ".txt":
            with open(file_path, "tr", encoding="utf8") as f:
                return f.read()
        else:
            return "File does not have a .txt extension."

    def create(self, data_input: str) -> dict:
        # Note: Delete from string characters "." and "," then transform in to
        # ordered list.
        words = data_input.casefold().replace(".", "").replace(",", "").split(" ")
        words.sort()
        # --- end note
        hist = {}

        for word in words:
            if word in hist:
                hist[word] += 1
            else:
                hist[word] = 1

        return hist

    def generate_report(self, histogram: dict, output_type: str = "html", path: str = "report") -> bool:
        output_types = ["html", "csv", "txt"]

        if output_type not in output_types:
            return False
        else:
            if output_type == "html":
                output = ["<html>\n<body>\n\t<table>\n\t<tr><th>Name</th>"
                          "<th>Amount</th></tr>"]

                for key in histogram.keys():
                    output.append("<tr><td>{key}</td><td>{value}</td></tr>"
                                  .format(key=key, value=histogram[key]))

                output.append("\n\t</table>\n</body>\n</html>")

                with open(path + ".html", mode="w+") as f:
                    x = "".join(output)

                    if f.write(x) > 0:
                        f.close()
                        return True
                    else:
                        f.close()
                        return False

            elif output_type == "txt":
                output = ["NAME\t\tVALUE\n"]

                for key in histogram.keys():
                    output.append("{key}\t\t{value}\n"
                                  .format(key=key, value=histogram[key]))

                with open(path + ".txt", mode="w+") as f:
                    x = "".join(output)

                    if f.write(x) > 0:
                        f.close()
                        return True
                    else:
                        f.close()
                        return False

            elif output_type == "csv":
                with open(path + ".csv", mode="w+", newline="") as csvfile:
                    fieldnames = ["name", "amount"]
                    writer = csv.writer(csvfile)

                    writer.writerow(fieldnames)

                    for key, value in histogram.items():
                        writer.writerow([key, value])

                    csvfile.close()

                    if writer:
                        return True
                    else:
                        return False


class HistogramJSON(HistogramInterface):
    def read_data(self, file_name: str) -> str:
        extension = file_name[file_name.rfind("."):]

        if extension == ".json":
            with open(file_name, "tr", encoding="utf8") as f:
                input_json = json.load(f)

                return input_json["data"]
        else:
            return "File does not have a .json extension."

    def create(self, data_input: str) -> dict:
        # Note: Delete from string characters "." and "," then transform in to
        # ordered list.
        words = data_input.casefold().replace(".", "").replace(",", "").split(" ")
        words.sort()
        # --- end note
        hist = {}

        for word in words:
            if word in hist:
                hist[word] += 1
            else:
                hist[word] = 1

        return hist

    def generate_report(self, histogram: dict, output_type: str = "html", path: str = "report") -> bool:
        output_types = ["html", "csv", "txt"]

        if output_type not in output_types:
            return False
        else:
            if output_type == "html":
                output = ["<html>\n<body>\n\t<table>\n\t<tr><th>Name</th>"
                          "<th>Amount</th></tr>"]

                for key in histogram.keys():
                    output.append("<tr><td>{key}</td><td>{value}</td></tr>"
                                  .format(key=key, value=histogram[key]))

                output.append("\n\t</table>\n</body>\n</html>")

                with open(path + ".html", mode="w+") as f:
                    x = "".join(output)

                    if f.write(x) > 0:
                        f.close()
                        return True
                    else:
                        f.close()
                        return False

            elif output_type == "txt":
                output = ["NAME\t\tVALUE\n"]

                for key in histogram.keys():
                    output.append("{key}\t\t{value}\n"
                                  .format(key=key, value=histogram[key]))

                with open(path + ".txt", mode="w+") as f:
                    x = "".join(output)

                    if f.write(x) > 0:
                        f.close()
                        return True
                    else:
                        f.close()
                        return False

            elif output_type == "csv":
                with open(path + ".csv", mode="w+", newline="") as csvfile:
                    fieldnames = ["name", "amount"]
                    writer = csv.writer(csvfile)

                    writer.writerow(fieldnames)

                    for key, value in histogram.items():
                        writer.writerow([key, value])

                    csvfile.close()

                    if writer:
                        return True
                    else:
                        return False


class HistogramXml(HistogramInterface):
    def read_data(self, file_name: str) -> str:
        extension = file_name[file_name.rfind("."):]

        if extension == ".xml":
            tree = ET.parse(file_name)
            root = tree.getroot()
            element = root.find("body")
            text = "".lstrip().join(element.itertext())

            return text.replace("\n", "")
        else:
            return "File does not have a .xml extension."

    def create(self, data_input: str) -> dict:
        # Note: Delete from string characters "." and "," then transform in to
        # ordered list.
        words = data_input.casefold().replace(".", "").replace(",", "").split(" ")
        words.sort()
        # --- end note
        hist = {}

        for word in words:
            if word in hist:
                hist[word] += 1
            else:
                hist[word] = 1

        return hist

    def generate_report(self, histogram: dict, output_type: str = "html", path: str = "report") -> bool:
        output_types = ["html", "csv", "txt"]

        if output_type not in output_types:
            return False
        else:
            if output_type == "html":
                output = ["<html>\n<body>\n\t<table>\n\t<tr><th>Name</th>"
                          "<th>Amount</th></tr>"]

                for key in histogram.keys():
                    output.append("<tr><td>{key}</td><td>{value}</td></tr>"
                                  .format(key=key, value=histogram[key]))

                output.append("\n\t</table>\n</body>\n</html>")

                with open(path + ".html", mode="w+") as f:
                    x = "".join(output)

                    if f.write(x) > 0:
                        f.close()
                        return True
                    else:
                        f.close()
                        return False

            elif output_type == "txt":
                output = ["NAME\t\tVALUE\n"]

                for key in histogram.keys():
                    output.append("{key}\t\t{value}\n"
                                  .format(key=key, value=histogram[key]))

                with open(path + ".txt", mode="w+") as f:
                    x = "".join(output)

                    if f.write(x) > 0:
                        f.close()
                        return True
                    else:
                        f.close()
                        return False

            elif output_type == "csv":
                with open(path + ".csv", mode="w+", newline="") as csvfile:
                    fieldnames = ["name", "amount"]
                    writer = csv.writer(csvfile)

                    writer.writerow(fieldnames)

                    for key, value in histogram.items():
                        writer.writerow([key, value])

                    csvfile.close()

                    if writer:
                        return True
                    else:
                        return False


if __name__ == '__main__':
    histo = HistogramTxt()
    data = histo.read_data("./data_source/sample.txt")
    histo.generate_report(histo.create(data), path="./reports/report_01")

    jsono = HistogramJSON()
    data2 = jsono.read_data("./data_source/sample.json")
    jsono.generate_report(jsono.create(data2), path="./reports/report_02")

    xmlo = HistogramXml()
    data2 = xmlo.read_data("./data_source/sample.xml")
    xmlo.generate_report(xmlo.create(data2), output_type="csv", path="./reports/report_03")
