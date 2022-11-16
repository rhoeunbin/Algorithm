while True: # 예외 처리 구문 : try~ except~문
    try: #(예외가 발생할 수도 있는 코드)
        print(input())
    except EOFError: #except : (예외가 발생했을 경우 실행되는 코드)
        break #EOFError : 입력이 끝남(End Of File) 에러
      
# 데이터가 없어 더 이상 값을 읽을 수 없을 때 발생하는 에러