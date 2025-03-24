  const donateToContract = async (amount) => {
  const provider = new ethers.providers.Web3Provider(window.ethereum);
  const contract = new ethers.Contract(contractAddress, contractABI, provider.getSigner());
  await contract.donate({ value: ethers.utils.parseEther(amount) });
};