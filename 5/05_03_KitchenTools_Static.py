"""
EXERCISE 5.3 - Static Methods

Shënim:
PDF-ja thotë: "Modify the program from task 2.2 so that the methods
of the class KitchenTools are static."

Programi i ushtrimit 2.2 nuk është pjesë e PDF-së së ngarkuar, prandaj
nuk mund të rikrijohet 1:1 pa shpikur metodat origjinale.

Më poshtë është modeli i saktë se si bëhet kthimi i metodave në static.
Zëvendëso emrat dhe trupat e metodave me ato të ushtrimit 2.2.
"""


class KitchenTools:
    @staticmethod
    def example_tool_action(tool_name: str) -> str:
        return f"Po përdoret mjeti: {tool_name}"


if __name__ == "__main__":
    # Me @staticmethod metoda thirret pa krijuar objekt.
    print(KitchenTools.example_tool_action("thikë"))
