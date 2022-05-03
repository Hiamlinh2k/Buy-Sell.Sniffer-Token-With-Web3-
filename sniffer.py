def sniffer():
    print(style.GREEN+"► How many BNB you want buy :",end='')
    value=str(input())
    print("Contract you Want sniffer : ",end='')
    ctb=str(input()) 

    def lock():

        try:

            BNBTokenAddress = Web3.toChecksumAddress(WBNB)  # BNB
            router = web3.eth.contract(address=Web3.toChecksumAddress(panrouter), abi=panabi)
            amountIn = web3.toWei(1, 'ether')
            amountOut = router.functions.getAmountsOut(amountIn, [Web3.toChecksumAddress(ctb), BNBTokenAddress]).call()
            amountOut = web3.fromWei(amountOut[1], 'ether')  
            b=amountOut
            while True :
                BNBTokenAddress = Web3.toChecksumAddress(WBNB)  # BNB
                router = web3.eth.contract(address=Web3.toChecksumAddress(panrouter), abi=panabi)
                amountIn = web3.toWei(1, 'ether')
                amountOut = router.functions.getAmountsOut(amountIn, [Web3.toChecksumAddress(ctb), BNBTokenAddress]).call()
                amountOut = web3.fromWei(amountOut[1], 'ether')
                if amountOut==b:
                    print("Waiting to buy ...")                   
                else:                        
                    tokenToBuy = web3.toChecksumAddress(ctb)
                    spend = web3.toChecksumAddress(WBNB)                         
                    contract = web3.eth.contract(address=panrouter, abi=panabi)
                    nonce = web3.eth.get_transaction_count(sender_address)                         
                    start = time.time()
                                                #Buy TOKEN 
                    pancakeswap2_txn = contract.functions.swapExactETHForTokens(
                    0, # set to 0, or specify minimum amount of tokeny you want to receive - consider decimals!!!
                    [spend,tokenToBuy],
                    sender_address,
                    (int(time.time()) + 10000)
                    ).buildTransaction({
                    'from': sender_address,
                    'value': web3.toWei(value,'ether'),
                    'gas':gaslimituse,
                    'gasPrice': web3.toWei(gaspriceuse,'gwei'),
                    'nonce': nonce,
                    })                           
                    signed_txn = web3.eth.account.sign_transaction(pancakeswap2_txn, private_key=key)
                    tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
                    print("► Sniffer Done HASH : "+"https://testnet.bscscan.com/tx/"+str(web3.toHex(tx_token)))
                    now = datetime.now()
                    print("Time : ", now.strftime("%d/%m/%Y %H:%M:%S"))
                    print("\n")
                    break
        except:
            ret=os.system('cls')
            print(style.RED+"ERROR , TRY AGAIN..."+style.RESET)
            print("\n")


    def unlock():
        while True:
            try:
                BNBTokenAddress = Web3.toChecksumAddress(WBNB)  # BNB
                router = web3.eth.contract(address=Web3.toChecksumAddress(panrouter), abi=panabi)
                amountIn = web3.toWei(1, 'ether')
                amountOut = router.functions.getAmountsOut(amountIn, [Web3.toChecksumAddress(ctb), BNBTokenAddress]).call()
                amountOut = web3.fromWei(amountOut[1], 'ether')  
                b=amountOut
                if b>0:
                    tokenToBuy = web3.toChecksumAddress(ctb)
                    spend = web3.toChecksumAddress(WBNB)                         
                    contract = web3.eth.contract(address=panrouter, abi=panabi)
                    nonce = web3.eth.get_transaction_count(sender_address)                         
                    start = time.time()
                                                    #Buy TOKEN 
                    pancakeswap2_txn = contract.functions.swapExactETHForTokens(
                    0, # set to 0, or specify minimum amount of tokeny you want to receive - consider decimals!!!
                    [spend,tokenToBuy],
                    sender_address,
                    (int(time.time()) + 10000)
                    ).buildTransaction({
                    'from': sender_address,
                    'value': web3.toWei(value,'ether'),
                    'gas':gaslimituse,
                    'gasPrice': web3.toWei(gaspriceuse,'gwei'),
                    'nonce': nonce,
                    })                           
                    signed_txn = web3.eth.account.sign_transaction(pancakeswap2_txn, private_key=key)
                    tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
                    print(style.GREEN+"► Sniffer Done HASH : "+"https://testnet.bscscan.com/tx/"+str(web3.toHex(tx_token)))
                    now = datetime.now()
                    print("Time : ", now.strftime("%d/%m/%Y %H:%M:%S"))
                    print("\n")
                    break
                else:
                    print("No liquidity ")
            except:
                print(style.RED+"ERROR , TRYING AGAIN..."+style.RESET)
