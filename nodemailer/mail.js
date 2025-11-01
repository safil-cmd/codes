var nodemailer = require('nodemailer');

var sender = nodemailer.createTransport({
service: 'gmail',
 auth: {
 user: 'salsafil9841268337@gmail.com',
 pass: 'kivwrwzxtrurnajn'
 }
});

function generateOTP() {
  return Math.floor(1000 + Math.random() * 9000);
}

function sendOTPEmail() {
const otp = generateOTP();
const compose = {
 from: 'salsafil9841268337@gmail.com',
to: 'majee.fathu@gmail.com',
 subject: '🔐 Your OTP Code',
 text: `Your OTP is: ${otp}`
 };

 sender.sendMail(compose, (error, info) => {
if (error) {
 console.error('Error sending OTP:', error);
} else {
console.log('OTP sent:', otp, '| SMTP response:', info.response);
}
 });
}

sendOTPEmail();
