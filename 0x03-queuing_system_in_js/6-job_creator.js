import {createQueue} from 'kue';

const push_notification_code = createQueue()
var job = push_notification_code.create('myjob',{
  phoneNumber: 'string',
  message: 'string',
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
