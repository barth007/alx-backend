import {createQueue} from 'kue';

const push_notification_code = createQueue()
var job = push_notification_code.create('myjob',{
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account',
}).save(err=>{
  if(!err){
    console.log('Notification job created:', job.id);
  }
}).on('failed', ()=>{
  console.log('Notification job failed')
})
.on('complete', ()=>{
  console.log('Notification job completed')
})

const sendNotification = (phoneNumber, message)=>{
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`)
}

push_notification_code.process('myjob', (job, done)=>{
  const {phoneNumber, message} = job.data;
  sendNotification(phoneNumber, message);
  done();
});
