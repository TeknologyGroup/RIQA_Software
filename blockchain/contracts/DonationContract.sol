
function donate() external payable {
    totalDonations += msg.value;
    emit Donated(msg.sender, msg.value);


}