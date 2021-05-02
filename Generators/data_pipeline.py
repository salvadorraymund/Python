import csv

file_name = "techcrunch.csv"
lines = (line for line in open(file_name))
list_line = (s.rstrip().split(",") for s in lines)
cols = next(list_line)
company_dicts = (dict(zip(cols, data)) for data in list_line)
funding = (
    int(company_dict["raisedAmt"])
    for company_dict in company_dicts
    if company_dict["round"] == "a"
)
# total_donation = (
#     len(company_dict["raisedAmt"])
#     for company_dict in company_dicts
#     if company_dict["round"] == ["a"]
# )


def total_donation():
    count = 0
    for company_dict["round"] in company_dicts:
        if company_dict["round"] == ["a"]:
            count += 1
    yield count


total_series_a = sum(funding)
# total_company_per_round = sum(total_donation)
# print(total_company_per_round)
# average_donation = total_series_a / total_company_per_round
print(f"Total series A fundraising: ${total_series_a}")
# print(f"The average donation per company is: ${average_donation}")
