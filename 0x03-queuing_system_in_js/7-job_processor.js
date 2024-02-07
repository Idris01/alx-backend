import kue from 'kue';

const queue = kue.createQueue();
const queName = 'push_notification_code_2';

const blackListNo = ['4153518780', '4153518781'];

function sendNotification (phoneNumber, message, job, done) {
  if (blackListNo.includes(phoneNumber)) {
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }
  const counter = 100;
  function next (num) {
    job.progress(num, counter);
    if (num === 50) done();
    else {
      console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
      next(num + 50);
    }
  }
  next(0);
}

queue.process(queName, 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
