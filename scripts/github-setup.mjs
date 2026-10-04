// Uses only Git's configured credential helper. Credentials stay in memory.
// No token is printed or saved by this script.
import { execFileSync } from 'node:child_process';

const action = process.argv[2] || 'check';
const owner = 'BetterCI', repo = 'n3-hearingpedia';
let token;
try {
  const credential = execFileSync('git', ['credential', 'fill'], {
    input: 'protocol=https\nhost=github.com\n\n', encoding: 'utf8', timeout: 15000,
    env: { ...process.env, GIT_TERMINAL_PROMPT: '0', GCM_INTERACTIVE: 'never' },
    stdio: ['pipe', 'pipe', 'pipe'],
  });
  token = credential.split(/\r?\n/).find(line => line.startsWith('password='))?.slice(9);
} catch {}
if (!token) { console.log(JSON.stringify({ authenticated: false, reason: 'No usable GitHub credential in configured Git helper' })); process.exit(2); }
async function api(path, method = 'GET', body) {
  const response = await fetch('https://api.github.com'+path, {
    method,
    headers: { Authorization: 'Bearer '+token, Accept: 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28', 'Content-Type': 'application/json' },
    body: body ? JSON.stringify(body) : undefined,
  });
  const data = await response.json().catch(() => ({}));
  return { status: response.status, data };
}
const user = await api('/user');
if (user.status !== 200) { console.log(JSON.stringify({authenticated:false,status:user.status}));process.exit(2); }
if (user.data.login.toLowerCase() !== owner.toLowerCase()) { console.log(JSON.stringify({authenticated:true,login:user.data.login,reason:'Credential account differs from requested owner'}));process.exit(3); }
const repoPath='/repos/'+owner+'/'+repo;
if (action === 'identity') {
  execFileSync('git', ['config', 'user.name', user.data.login]);
  execFileSync('git', ['config', 'user.email', user.data.id+'+'+user.data.login+'@users.noreply.github.com']);
  console.log(JSON.stringify({ configured: true, account: user.data.login, emailType: 'GitHub noreply' }));
} else if (action === 'check') {
  const result=await api(repoPath);
  console.log(JSON.stringify({authenticated:true,login:user.data.login,repoStatus:result.status,repository:result.data.full_name,permissions:result.data.permissions}));
} else if (action === 'create') {
  const existing=await api(repoPath);
  if(existing.status===200) { console.log(JSON.stringify({created:false,existing:true,url:existing.data.html_url}));process.exit(0); }
  if(existing.status!==404) { console.log(JSON.stringify({created:false,status:existing.status}));process.exit(4); }
  const result=await api('/user/repos','POST',{name:repo,description:'连接听觉机制、感知与工程的专业百科 | An evidence-linked knowledge network for hearing science',private:false,auto_init:false,homepage:'https://betterci.github.io/n3-hearingpedia/'});
  console.log(JSON.stringify({created:result.status===201,status:result.status,url:result.data.html_url,message:result.data.message}));
  if(result.status!==201)process.exit(4);
} else if (action === 'pages') {
  let result=await api(repoPath+'/pages');
  if(result.status===404)result=await api(repoPath+'/pages','POST',{build_type:'workflow'});
  else if(result.status===200&&result.data.build_type!=='workflow')result=await api(repoPath+'/pages','PUT',{build_type:'workflow'});
  console.log(JSON.stringify({status:result.status,url:result.data.html_url,buildType:result.data.build_type,message:result.data.message}));
  if(![200,201,204].includes(result.status))process.exit(4);
} else if (action === 'metadata') {
  const result=await api(repoPath,'PATCH',{description:'连接听觉机制、感知与工程的专业百科 | An evidence-linked knowledge network for hearing science',homepage:'https://betterci.github.io/n3-hearingpedia/'});
  console.log(JSON.stringify({status:result.status,description:result.data.description,homepage:result.data.homepage}));
  if(result.status!==200)process.exit(4);
} else if (action === 'status') {
  const result=await api(repoPath+'/actions/runs?per_page=3');
  console.log(JSON.stringify({status:result.status,runs:result.data.workflow_runs?.map(r=>({id:r.id,status:r.status,conclusion:r.conclusion,url:r.html_url,sha:r.head_sha}))}));
} else throw new Error('Unknown action');
