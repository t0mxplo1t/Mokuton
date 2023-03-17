import phonenumbers as pnumb

from phonenumbers import parse
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

def banner():
	print("""
\033[95m_  _ ____ _  _ _  _ ___ ____ _  _\033[0m
\033[95m|\/| |  | |_/  |  |  |  |  | |\ | \033[93mv1.4\033[0m
\033[95m|  | |__| | \_ |__|  |  |__| | \|\033[0m
+--------------------------------+
| \033[104m#https://github.com/14sept2002\033[0m |
+--------------------------------+""")
banner()

number = input("\n\033[92mEnter a number \033[0m[\033[101m+62\033[0m] \033[0m: ")
parsing = parse(number)
loc = geocoder.description_for_number(parsing,"id")
isp = carrier.name_for_number(parsing,"id")
tz = timezone.time_zones_for_number(parsing)

print("\033[92mInfo \033[0m:",parsing)
print("\033[92mFormat internasional \033[0m:",pnumb.normalize_digits_only(parsing))
print("\033[92mFormat nasional \033[0m:",pnumb.national_significant_number(parsing))
print("\033[92mNomornya valid \033[0m:",pnumb.is_valid_number(parsing))
print("\033[92mDapat dihubungi secara internasional \033[0m:",pnumb.can_be_internationally_dialled(parsing))
print("\033[92mLokasi \033[0m:",loc)
print("\033[92mKode wilayah nomor \033[0m:",pnumb.region_code_for_number(parsing))
print("\033[92mJenis nomor \033[0m:",pnumb.number_type(parsing))
print("\033[92mApakah operator tertentu \033[0m:",pnumb.is_carrier_specific(parsing))
print("\033[92mISP \033[0m:",isp)
print("\033[92mZona waktu \033[0m:",tz)
print("\033[92mTermasuk nomor geografis \033[0m:",pnumb.is_number_geographical(parsing))
