from helpers import dotenv, runtime
from run_ui import run


if __name__ == "__main__":
      runtime.initialize()
      dotenv.load_dotenv()
      run()
  
