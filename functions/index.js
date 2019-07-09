const functions = require('firebase-functions');
const admin = require('firebase-admin');
const nodemailer = require('nodemailer');
const cors = require('cors')({ origin: true });

admin.initializeApp();

exports.forwardMessage = functions.https.onRequest((req, res) => {
  cors(req, res, () => {
    const fromEmail = req.body.email;
    const fromName = req.body.name;
    const fromMessage = req.body.message;
    const mailOptions = {
        from: `${fromName} <${fromEmail}>`,
        to: `Aaron C <aaronc@protonmail.ch>`,
        subject: 'aaronc.ca contact form auto forwarder',
        html: `<p>Hey Man!</p>
<p>The message:</p>
<pre>${fromMessage}</pre>`
    };
    const transporter = nodemailer.createTransport({
        service: 'gmail',
        auth: functions.config().gmail
    });
    return transporter.sendMail(mailOptions, (err, info) => {
      if (err) return res.send(err.toString());
      return res.send(req.body);
    });
  });
});

exports.responseMessage = functions.https.onRequest((req, res) => {
  cors(req, res, () => {
    const senderEmail = req.body.email;
    const senderName = req.body.name;
    const senderMessage = req.body.message;
    const mailOptions = {
        from: 'aaronc <aaronc@protonmail.ch>',
        to: `${senderName} <${senderEmail}>`,
        subject: 'aaronc.ca contact form auto responder',
        html: `<p>Hello, ${senderName}!</p>
<p>Thanks for getting in touch!</br>
Your message has been forwarded, and I will get back to you ASAP!</p>
<p>In the mean time, feel free to text me at 289-213-3228</p>
<p><em>Have an amazing day!</em></p>
<hr />
<p>Your message:</p>
<pre>${senderMessage}</pre>`
    };
    const transporter = nodemailer.createTransport({
        service: 'gmail',
        auth: functions.config().gmail
    });
    return transporter.sendMail(mailOptions, (err, info) => {
      if (err) return res.send(err.toString());
      return res.send(req.body);
    });
  });
});
