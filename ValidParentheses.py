target = input("enter brackets")

all_strings = [
    "()", "{}", "[]",
    "({})", "[()]", "{[]}",
    "({[]})", "[{()}]", "{[()]}",
    "([{}])", "{({})}", "[([])]",
    "({{[]}})", "[({[]})]", "{{[({})]}}",
    "({[({})]})", "[{({[]})}]", "{([([])])}",
    "([({[]})])", "{{([{}])}}"
]

if target in all_strings:
    print("valid")
else:
    print("invalid")









class Solution:
    def isValid(self, s: str) -> bool:
        # Tumhari saari patterns list
        patterns = [
            "()", "{}", "[]",
            "({})", "[()]", "{[]}",
            "({[]})", "[{()}]", "{[()]}",
            "([{}])", "{({})}", "[([])]",
            "({{[]}})", "[({[]})]", "{{[({})]}}",
            "({[({})]})", "[{({[]})}]", "{([([])])}",
            "([({[]})])", "{{([{}])}}"
        ]
        if s in patterns:
            return True
        return False
