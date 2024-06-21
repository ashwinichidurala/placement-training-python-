#how many  years  weeks months days
total_days = int(input())


years = total_days // 360
months = (total_days % 360) // 30
weeks = (total_days % 30) // 7
days = total_days % 7


print(f"{years}y\\{months}m\\{weeks}w\\{days}d")
