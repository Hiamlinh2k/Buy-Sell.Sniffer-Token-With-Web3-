tokenToBuy = web3.toChecksumAddress(ctb)
spend = web3.toChecksumAddress(WBNB)

contract = web3.eth.contract(address=panrouter, abi=panabi)
nonce = web3.eth.get_transaction_count(sender_address)                         
start = time.time()
                                                            #Buy TOKEN 
pancakeswap2_txn = contract.functions.swapExactETHForTokensSupportingFeeOnTransferTokens(
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
print("► Buy "+" Done HASH : "+"https://testnet.bscscan.com/tx/"+str(web3.toHex(tx_token)))
now = datetime.now()
buytokencontract=web3.eth.contract(ctb,abi=sellAbi)
symbol=buytokencontract.functions.symbol().call()
name = buytokencontract.functions.name().call()

print("The token : "+name+"("+symbol+")"+"&"+"Time : ", now.strftime("%d/%m/%Y %H:%M:%S"))
print("\n")