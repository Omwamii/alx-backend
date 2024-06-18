import { createQueue } from "kue";

// Create a Kue queue
const queue = createQueue();

// Create job data object
const jobData = {
  phoneNumber: '1234567890',
  message: 'Hello, this is a test notification',
};

// Create a job in the queue named push_notification_code
const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (err) {
      console.error('Notification job failed to create');
      return;
    }
    console.log(`Notification job created: ${job.id}`);
  });

// Event listener for job completion
job.on('complete', () => {
  console.log('Notification job completed');
});

// Event listener for job failure
job.on('failed', () => {
  console.log('Notification job failed');
});
