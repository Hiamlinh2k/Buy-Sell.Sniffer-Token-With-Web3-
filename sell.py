tokenValue = web3.toWei(valuesell, 'ether')
tokenValue2 = web3.fromWei(tokenValue, 'ether')
                                                                                    #Approved
start = time.time()
approve = sellTokenContract.functions.approve(panrouter, balance).buildTransaction({
'from': sender_address,
'gas': gaslimituse,
'gasPrice': web3.toWei(gaspriceuse,'gwei'),
'nonce': web3.eth.get_transaction_count(sender_address),
})
signed_txn = web3.eth.account.sign_transaction(approve, private_key=key)
tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
print("Approved: " + web3.toHex(tx_token))

time.sleep(10)

print(f"► Swapping {tokenValue2} {symbol} for BNB...")
print("► Waiting Swap...")

                                                                                    #Swaping exact Token for ETH 
spend = web3.toChecksumAddress(WBNB)
contract = web3.eth.contract(address=panrouter, abi=panabi)
pancakeswap2_txn = contract.functions.swapExactTokensForETH(
    tokenValue ,0, 
    [contract_id, spend],
    sender_address,
    (int(time.time()) + 1000000)
    ).buildTransaction({
    'from': sender_address,
    'gas': gaslimituse,
    'gasPrice': web3.toWei(gaspriceuse,'gwei'),
    'nonce': web3.eth.get_transaction_count(sender_address),
    })
signed_txn = web3.eth.account.sign_transaction(pancakeswap2_txn,private_key=key)
tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)  
print(f"► Sold {symbol} Done Hash: "+"https://testnet.bscscan.com/tx/"+ web3.toHex(tx_token))
now = datetime.now()
print("Time : ", now.strftime("%d/%m/%Y %H:%M:%S")+style.RESET)
print("\n")