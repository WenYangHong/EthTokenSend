#!/usr/bin/env python
from flask import Flask
from web3 import Web3,HTTPProvider
import json
import os
app = Flask(__name__)

@app.route("/api/send/<string:address>/<float:count>")
def hello(address,count):
    the_abi = """
    [
        {
          "constant": true,
          "inputs": [],
          "name": "name",
          "outputs": [
            {
              "name": "",
              "type": "string"
            }
          ],
          "payable": false,
          "stateMutability": "view",
          "type": "function"
        },
        {
          "constant": false,
          "inputs": [
            {
              "name": "_spender",
              "type": "address"
            },
            {
              "name": "_value",
              "type": "uint256"
            }
          ],
          "name": "approve",
          "outputs": [
            {
              "name": "",
              "type": "bool"
            }
          ],
          "payable": false,
          "stateMutability": "nonpayable",
          "type": "function"
        },
        {
          "constant": true,
          "inputs": [],
          "name": "totalSupply",
          "outputs": [
            {
              "name": "",
              "type": "uint256"
            }
          ],
          "payable": false,
          "stateMutability": "view",
          "type": "function"
        },
        {
          "constant": false,
          "inputs": [
            {
              "name": "_from",
              "type": "address"
            },
            {
              "name": "_to",
              "type": "address"
            },
            {
              "name": "_value",
              "type": "uint256"
            }
          ],
          "name": "transferFrom",
          "outputs": [
            {
              "name": "",
              "type": "bool"
            }
          ],
          "payable": false,
          "stateMutability": "nonpayable",
          "type": "function"
        },
        {
          "constant": true,
          "inputs": [],
          "name": "decimals",
          "outputs": [
            {
              "name": "",
              "type": "uint8"
            }
          ],
          "payable": false,
          "stateMutability": "view",
          "type": "function"
        },
        {
          "constant": false,
          "inputs": [
            {
              "name": "_value",
              "type": "uint256"
            }
          ],
          "name": "burn",
          "outputs": [],
          "payable": false,
          "stateMutability": "nonpayable",
          "type": "function"
        },
        {
          "constant": false,
          "inputs": [
            {
              "name": "_spender",
              "type": "address"
            },
            {
              "name": "_subtractedValue",
              "type": "uint256"
            }
          ],
          "name": "decreaseApproval",
          "outputs": [
            {
              "name": "",
              "type": "bool"
            }
          ],
          "payable": false,
          "stateMutability": "nonpayable",
          "type": "function"
        },
        {
          "constant": true,
          "inputs": [
            {
              "name": "_owner",
              "type": "address"
            }
          ],
          "name": "balanceOf",
          "outputs": [
            {
              "name": "",
              "type": "uint256"
            }
          ],
          "payable": false,
          "stateMutability": "view",
          "type": "function"
        },
        {
          "constant": true,
          "inputs": [],
          "name": "symbol",
          "outputs": [
            {
              "name": "",
              "type": "string"
            }
          ],
          "payable": false,
          "stateMutability": "view",
          "type": "function"
        },
        {
          "constant": false,
          "inputs": [
            {
              "name": "_to",
              "type": "address"
            },
            {
              "name": "_value",
              "type": "uint256"
            }
          ],
          "name": "transfer",
          "outputs": [
            {
              "name": "",
              "type": "bool"
            }
          ],
          "payable": false,
          "stateMutability": "nonpayable",
          "type": "function"
        },
        {
          "constant": false,
          "inputs": [
            {
              "name": "_spender",
              "type": "address"
            },
            {
              "name": "_addedValue",
              "type": "uint256"
            }
          ],
          "name": "increaseApproval",
          "outputs": [
            {
              "name": "",
              "type": "bool"
            }
          ],
          "payable": false,
          "stateMutability": "nonpayable",
          "type": "function"
        },
        {
          "constant": true,
          "inputs": [
            {
              "name": "_owner",
              "type": "address"
            },
            {
              "name": "_spender",
              "type": "address"
            }
          ],
          "name": "allowance",
          "outputs": [
            {
              "name": "",
              "type": "uint256"
            }
          ],
          "payable": false,
          "stateMutability": "view",
          "type": "function"
        },
        {
          "inputs": [],
          "payable": false,
          "stateMutability": "nonpayable",
          "type": "constructor"
        },
        {
          "anonymous": false,
          "inputs": [
            {
              "indexed": true,
              "name": "burner",
              "type": "address"
            },
            {
              "indexed": false,
              "name": "value",
              "type": "uint256"
            }
          ],
          "name": "Burn",
          "type": "event"
        },
        {
          "anonymous": false,
          "inputs": [
            {
              "indexed": true,
              "name": "owner",
              "type": "address"
            },
            {
              "indexed": true,
              "name": "spender",
              "type": "address"
            },
            {
              "indexed": false,
              "name": "value",
              "type": "uint256"
            }
          ],
          "name": "Approval",
          "type": "event"
        },
        {
          "anonymous": false,
          "inputs": [
            {
              "indexed": true,
              "name": "from",
              "type": "address"
            },
            {
              "indexed": true,
              "name": "to",
              "type": "address"
            },
            {
              "indexed": false,
              "name": "value",
              "type": "uint256"
            }
          ],
          "name": "Transfer",
          "type": "event"
        }
      ]"""
    web3 = Web3(HTTPProvider("http://localhost:8545"))
    if (count <= 0):
        return json.dumps({"code": 403, "msg": "token count to low"})
    if (web3.isAddress(address) != True):
        return json.dumps({"code": 403, "msg": "Address is worng"})
    web3.personal.unlockAccount(web3.eth.accounts[0], '123456')
    abi = json.loads(the_abi)
    my_contract = web3.eth.contract(abi=abi)
    the_contract = my_contract("0x538F2F2eB7B9B0c6B2748314063383371a2Ba5F1")
    # 执行打币脚本
    hash = the_contract.transact({
        "from": web3.eth.accounts[0],
        'gas':52146,
        'gasPrice':web3.toWei(10,'gwei')
    }).transfer(address, web3.toWei(count, "ether"))
    return json.dumps({"code": 200, "msg": "send ok", "hash": hash})

@app.route("/api/checkIfHaveOrder/<float:amount>/<int:checked>/<string:name>/<string:short>/<int:decimal>/<int:totalSupply>")
# amount订单总额,用于查询订单  checked 查询完成的区块号
def checkIfHasOrder(amount,checked,name,short,decimal,totalSupply):
    flag = "no search"
    _from = "no address"
    _hash = ""
    _value = 0.0
    tx_hash = ""
    web3 = Web3(HTTPProvider("http://localhost:8545"))
    # 获取当前区块号
    blockNumber = web3.eth.blockNumber
    # 获取所有数据
    for i in range(checked,blockNumber):
        transaction = web3.eth.getBlock(i,full_transactions=True)
        # 到时候接收用户钱的地址
        address = "0x82E2Bc1f01D4Ace094Ac7022fd7bb4Ff035718a6"
        transactionArray = transaction.transactions

        for index in range(len(transactionArray)):
            # 如果交易里面包含我们设定的帐号则进行下一步
            if transactionArray[index].to == address:
                # 获取订单状态为 status = 1的订单
                receipt = web3.eth.getTransactionReceipt(transactionArray[index].hash)
                # 如果订单的状态为1则表示正常

                if abs(receipt.status - 1) < 1e-9:
                    if abs(transactionArray[index].value-web3.toWei(amount,'ether'))< 10 :
                        # 如果交易金额是和传递进来的参数一直则返回yes
                        flag = "yes"
                        # 如果正确将钱转移到另一个账户
                        returnAmount("0xb6e270A1B8e5D1F0Eaaa98C92815B893f9128D51",0.002,2)
                        # 如果正确生成sol文件
                        tx_hash = solMake(name,short,decimal,totalSupply)
                    else:
                        # 金额不一致有问题,返回用户金额
                        flag = "no"
                        if abs(transactionArray[index].value - web3.toWei(0.001,'ether')) > 10:
                            # 金额大于0.001的时候将0.001eth打入我们打入我们的账户
                            returnAmount("0xb6e270A1B8e5D1F0Eaaa98C92815B893f9128D51",0.001,1)
                            # 剩下的返回给用户
                            returnAmount(transactionArray[index]['from'],float(web3.fromWei(transactionArray[index].value,'ether')) - 0.001,1)
                #     返回打币地址和交易信息
                _from = transactionArray[index]['from']
                _hash = transactionArray[index].hash
                _value = web3.fromWei(transactionArray[index].value,'ether')
                return json.dumps({"code":200,"msg":flag,"checkedBlockNumber":blockNumber,'_from':_from,'_hash':_hash,'_value':float(_value),'_tx_hash':tx_hash})

    return json.dumps({"code":200,"msg":flag,"checkedBlockNumber":blockNumber,'_from':_from,'_hash':_hash,'_value':float(_value),'_tx_hash':tx_hash})


# 进行金额的操作
def returnAmount(toAddress,amount,typeNumber):
    web3 = Web3(HTTPProvider("http://localhost:8545"))
    web3.personal.unlockAccount("0x82E2Bc1f01D4Ace094Ac7022fd7bb4Ff035718a6","123456")
#     进行返款的操作
    if(web3.isAddress(toAddress)):
    #     开始进行返款操作
        if typeNumber == 1:
            data = web3.toHex(text="金额有误退回账户")
        else:
            data = web3.toHex(text="有效订单,收入转入")
        hash = web3.eth.sendTransaction({'to':toAddress,'from':"0x82E2Bc1f01D4Ace094Ac7022fd7bb4Ff035718a6",'value':web3.toWei(amount,'ether'),'data':data})
        return json.dumps({"code":200,"msg":"transaction is ok","hash":hash})
    else:
        return json.dumps({"code":403,"msg":"address is wrong"})

# 获取最新的区块号
@app.route("/api/latestBlockNumber")
def latestBlockNumber():
    web3 = Web3(HTTPProvider("http://localhost:8545"))
    return json.dumps({"code":200,'data':str(web3.eth.blockNumber)})

# 进行sol文件的制作
def solMake(name,short,decimal,totalSupply_):
    folder = os.path.exists("/send/sol")
    if not folder:
        os.mkdir("/send/sol",777)
    sol = "/send/sol/"+name+'.sol'
    file = open(sol,'w')
    file.write('pragma solidity ^0.4.18;\n'
               'import "./zeppelin-solidity/contracts/token/ERC20/BurnableToken.sol";\n'
               'import "./zeppelin-solidity/contracts/token/ERC20/DetailedERC20.sol";\n'
               'import "./zeppelin-solidity/contracts/token/ERC20/StandardToken.sol";\n'
               'contract COLAcoin is BurnableToken, DetailedERC20, StandardToken {\n'
               '\tfunction COLAcoin() DetailedERC20("'+name+'", "'+short+'", '+str(decimal)+') public\n'
               '\t{\n'
               '\t\ttotalSupply_ = '+str(totalSupply_)+' * 1000000000000000000;\n'
               '\t\tbalances[msg.sender] = totalSupply_;\n'
               '\t}\n'
               '}')
    file.close()
    # 开始部署智能合约
    tx_hash = deploy(name)
    return tx_hash


# 部署智能合约
def deploy(path):
    web3 = Web3(HTTPProvider("http://localhost:8545"))
    web3.personal.unlockAccount("0x82E2Bc1f01D4Ace094Ac7022fd7bb4Ff035718a6","123456")
    # web3.personal.unlockAccount("0x736E12498fce01c8858B607fa2FC6349826533C1","123456")
    from solc import compile_source, compile_files, link_code
    compiled_sol        = compile_files(['./sol/' + path + '.sol'])
    contract_interface  = compiled_sol['./sol/' + path + '.sol:COLAcoin']
    contract            = web3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
    # 进行合约的部署
    tx_hash = contract.deploy(transaction={'from':"0x82E2Bc1f01D4Ace094Ac7022fd7bb4Ff035718a6", 'gas': 5000000,'gasPrice':web3.toWei(20,'gwei')})
    # tx_hash = contract.deploy(transaction={'from':"0x736E12498fce01c8858B607fa2FC6349826533C1", 'gas': 5000000,'gasPrice':web3.toWei(20,'gwei')})
    return tx_hash
    # return "caonima"

# 用来查询交易的数据获取token的address
@app.route("/api/getContractAddress/<string:tx_hash>")
def getTokenAddress(tx_hash):
    # tx_hash交易的hash值
    web3 = Web3(HTTPProvider("http://localhost:8545"))
    token = web3.eth.getTransactionReceipt(tx_hash)
    if token:
        # 返回token的地址
        return json.dumps({'code':200,'msg':'ok','data':token.contractAddress})
    return json.dumps({'code':403,'msg':'ok'})

@app.route("/api/successTokenSend/<string:address>/<string:tokenAddress>/<string:data>")
# 接收用户的地址:address  数量:count 创始信息:data 合约地址:tokenAddress
def successTokenSend(address,tokenAddress,data):
    the_abi = """
    [
        {
          "constant": true,
          "inputs": [],
          "name": "name",
          "outputs": [
            {
              "name": "",
              "type": "string"
            }
          ],
          "payable": false,
          "stateMutability": "view",
          "type": "function"
        },
        {
          "constant": false,
          "inputs": [
            {
              "name": "_spender",
              "type": "address"
            },
            {
              "name": "_value",
              "type": "uint256"
            }
          ],
          "name": "approve",
          "outputs": [
            {
              "name": "",
              "type": "bool"
            }
          ],
          "payable": false,
          "stateMutability": "nonpayable",
          "type": "function"
        },
        {
          "constant": true,
          "inputs": [],
          "name": "totalSupply",
          "outputs": [
            {
              "name": "",
              "type": "uint256"
            }
          ],
          "payable": false,
          "stateMutability": "view",
          "type": "function"
        },
        {
          "constant": false,
          "inputs": [
            {
              "name": "_from",
              "type": "address"
            },
            {
              "name": "_to",
              "type": "address"
            },
            {
              "name": "_value",
              "type": "uint256"
            }
          ],
          "name": "transferFrom",
          "outputs": [
            {
              "name": "",
              "type": "bool"
            }
          ],
          "payable": false,
          "stateMutability": "nonpayable",
          "type": "function"
        },
        {
          "constant": true,
          "inputs": [],
          "name": "decimals",
          "outputs": [
            {
              "name": "",
              "type": "uint8"
            }
          ],
          "payable": false,
          "stateMutability": "view",
          "type": "function"
        },
        {
          "constant": false,
          "inputs": [
            {
              "name": "_value",
              "type": "uint256"
            }
          ],
          "name": "burn",
          "outputs": [],
          "payable": false,
          "stateMutability": "nonpayable",
          "type": "function"
        },
        {
          "constant": false,
          "inputs": [
            {
              "name": "_spender",
              "type": "address"
            },
            {
              "name": "_subtractedValue",
              "type": "uint256"
            }
          ],
          "name": "decreaseApproval",
          "outputs": [
            {
              "name": "",
              "type": "bool"
            }
          ],
          "payable": false,
          "stateMutability": "nonpayable",
          "type": "function"
        },
        {
          "constant": true,
          "inputs": [
            {
              "name": "_owner",
              "type": "address"
            }
          ],
          "name": "balanceOf",
          "outputs": [
            {
              "name": "",
              "type": "uint256"
            }
          ],
          "payable": false,
          "stateMutability": "view",
          "type": "function"
        },
        {
          "constant": true,
          "inputs": [],
          "name": "symbol",
          "outputs": [
            {
              "name": "",
              "type": "string"
            }
          ],
          "payable": false,
          "stateMutability": "view",
          "type": "function"
        },
        {
          "constant": false,
          "inputs": [
            {
              "name": "_to",
              "type": "address"
            },
            {
              "name": "_value",
              "type": "uint256"
            }
          ],
          "name": "transfer",
          "outputs": [
            {
              "name": "",
              "type": "bool"
            }
          ],
          "payable": false,
          "stateMutability": "nonpayable",
          "type": "function"
        },
        {
          "constant": false,
          "inputs": [
            {
              "name": "_spender",
              "type": "address"
            },
            {
              "name": "_addedValue",
              "type": "uint256"
            }
          ],
          "name": "increaseApproval",
          "outputs": [
            {
              "name": "",
              "type": "bool"
            }
          ],
          "payable": false,
          "stateMutability": "nonpayable",
          "type": "function"
        },
        {
          "constant": true,
          "inputs": [
            {
              "name": "_owner",
              "type": "address"
            },
            {
              "name": "_spender",
              "type": "address"
            }
          ],
          "name": "allowance",
          "outputs": [
            {
              "name": "",
              "type": "uint256"
            }
          ],
          "payable": false,
          "stateMutability": "view",
          "type": "function"
        },
        {
          "inputs": [],
          "payable": false,
          "stateMutability": "nonpayable",
          "type": "constructor"
        },
        {
          "anonymous": false,
          "inputs": [
            {
              "indexed": true,
              "name": "burner",
              "type": "address"
            },
            {
              "indexed": false,
              "name": "value",
              "type": "uint256"
            }
          ],
          "name": "Burn",
          "type": "event"
        },
        {
          "anonymous": false,
          "inputs": [
            {
              "indexed": true,
              "name": "owner",
              "type": "address"
            },
            {
              "indexed": true,
              "name": "spender",
              "type": "address"
            },
            {
              "indexed": false,
              "name": "value",
              "type": "uint256"
            }
          ],
          "name": "Approval",
          "type": "event"
        },
        {
          "anonymous": false,
          "inputs": [
            {
              "indexed": true,
              "name": "from",
              "type": "address"
            },
            {
              "indexed": true,
              "name": "to",
              "type": "address"
            },
            {
              "indexed": false,
              "name": "value",
              "type": "uint256"
            }
          ],
          "name": "Transfer",
          "type": "event"
        }
      ]"""
    web3 = Web3(HTTPProvider("http://localhost:8545"))
    web3.personal.unlockAccount("0x82E2Bc1f01D4Ace094Ac7022fd7bb4Ff035718a6", '123456')
    abi = json.loads(the_abi)
    my_contract = web3.eth.contract(abi=abi)
    the_contract = my_contract(tokenAddress)
    # 执行打币脚本
    hash = the_contract.transact({
        "from": "0x82E2Bc1f01D4Ace094Ac7022fd7bb4Ff035718a6",
        'gas': 52146,
        'gasPrice': web3.toWei(10, 'gwei')
    }).transfer(address, web3.toWei(the_contract.call().totalSupply(), "ether"))
    return json.dumps({"code": 200, "msg": "send ok", "hash": hash})

if __name__ == "__main__":
    app.run(debug=True)


