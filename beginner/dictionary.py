monthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

june = "Jun"
print(monthConversion["Jan"])
print(monthConversion[june])
print(monthConversion.get("Oct"), "is fine")
print(monthConversion.get("Octs"), "is not fine")
print(monthConversion.get("Octs", "has not a valid key"))
