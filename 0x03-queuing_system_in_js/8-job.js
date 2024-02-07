const queueName = 'push_notification_code_3';

function createPushNotificationsJobs (jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }
  for (const jobData of jobs) {
    const job = queue.create(queueName, jobData)
      .save((err) => {
        if (!err) console.log(`Notification job created: ${job.id}`);
      });
    job.on('complete', () => console.log(`Notification job ${job.id} completed`))
      .on('failed', (err) => console.log(`Notification job ${job.id} failed: ${err}`))
      .on('progress', (prog) => console.log(`Notification job ${job.id} ${prog}% complete`));
  }
}

module.exports = createPushNotificationsJobs;
