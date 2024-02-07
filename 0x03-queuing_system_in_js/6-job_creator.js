import kue from 'kue';

const push_notification_code = kue.createQueue();
const jobData = {
  phoneNumber: '+2348181',
  message: 'Hello!!!'
};

const job = push_notification_code.create(
  'notify', jobData).save((err) => {
  if (!err) console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => console.log('Notification job completed'))
  .on('failed', () => console.log('Notification job failed'));
