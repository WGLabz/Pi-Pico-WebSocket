import uasyncio as a
from main_f import read_loop, send_telemetry

async def main():

    tasks = [read_loop(), send_telemetry()]
    await a.gather(*tasks)

a.run(main())
