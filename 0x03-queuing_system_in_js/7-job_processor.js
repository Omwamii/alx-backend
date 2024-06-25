import { createQueue, Job } from 'kue';

const queue = createQueue();

// Array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Function to send notification
function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);

  if (blacklistedNumbers.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
}

// Process jobs from the queue
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});

// Event listeners for job processing
queue.on('job enqueue', (id, type) => {
  Job.get(id, (err, job) => {
    if (err) return;
    console.log(`Notification job #${job.id} 0% complete`);
  });
}).on('job complete', (id, result) => {
  Job.get(id, (err, job) => {
    if (err) return;
    console.log(`Notification job #${job.id} completed`);
    job.remove(err => {
      if (err) throw err;
    });
  });
}).on('job failed', (id, errorMessage) => {
  Job.get(id, (err, job) => {
    if (err) return;
    console.log(`Notification job #${job.id} failed: ${errorMessage}`);
  });
}).on('job progress', (id, progress) => {
  Job.get(id, (err, job) => {
    if (err) return;
    console.log(`Notification job #${job.id} ${progress}% complete`);
  });
});
