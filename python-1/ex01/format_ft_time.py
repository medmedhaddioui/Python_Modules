import datetime
import time

epoch_time = time.time()
time_now = datetime.datetime.now()

print(f"Seconds since January 1, 1970:", end= " ")
print(f"{epoch_time:,.4f} or {epoch_time:.2e} in scientific notation")
print(time_now.strftime("%b %d %Y"))