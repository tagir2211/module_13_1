import asyncio
import datetime

def start_strm(funk):
  async def wrapper(*args):
    print(f'Силач {args[0]} начал соревнование')
    start = datetime.datetime.now()
    await funk(*args)
    end = datetime.datetime.now()
    print(f'Силач {args[0]} закончил соревнование за {end - start} секунд')
    
  return wrapper

@start_strm
async def start_strongman(name, power):
  for i in range(1, 6):
    await asyncio.sleep(1/power)
    print(f'Силач {name} поднял {i} шар')

async def main_():
  task1 = asyncio.create_task(start_strongman('Pasha', 1))
  task2 = asyncio.create_task(start_strongman('Denis', 0.2))
  task3 = asyncio.create_task(start_strongman('Apollon', 5))
  await task1
  await task2
  await task3

asyncio.run(main_())