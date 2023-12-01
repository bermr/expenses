import os
from pynubank import Nubank
from dotenv import load_dotenv

load_dotenv()

nu = Nubank()
uuid, qr_code = nu.get_qr_code()
qr_code.print_ascii(invert=True)

input('Press ENTER after scanning QR Code')

nu.authenticate_with_qr_code(os.getenv('CPF'), os.getenv('PASSWORD'), uuid)

print(nu.get_account_balance())

