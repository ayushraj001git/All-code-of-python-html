import React, { useState, useEffect } from 'react';
import { 
  Activity, Users, FileText, Stethoscope, Settings, Bell, Search, 
  Wifi, WifiOff, Globe, User, ChevronRight, AlertCircle, CheckCircle, 
  RefreshCw, Play, ArrowRight, Phone, Video
} from 'lucide-react';
import { 
  LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, BarChart, Bar 
} from 'recharts';

// --- MOCK DATA ---
const analyticsData = [
  { name: 'Mon', referrals: 4, followUps: 3 },
  { name: 'Tue', referrals: 3, followUps: 5 },
  { name: 'Wed', referrals: 6, followUps: 4 },
  { name: 'Thu', referrals: 5, followUps: 7 },
  { name: 'Fri', referrals: 8, followUps: 6 },
  { name: 'Sat', referrals: 2, followUps: 2 },
  { name: 'Sun', referrals: 1, followUps: 1 },
];

const REFERRAL_STAGES = [
  'Created', 'Sent', 'Received', 'Consultation', 'Outcome Recorded', 'Closed'
];

export default function MediReachApp() {
  // --- STATE ---
  const [currentView, setCurrentView] = useState('landing');
  const [isOffline, setIsOffline] = useState(false);
  const [syncQueue, setSyncQueue] = useState(0);
  const [isSyncing, setIsSyncing] = useState(false);
  const [demoMode, setDemoMode] = useState(false);
  const [referralStep, setReferralStep] = useState(0);
  const [toast, setToast] = useState<{message: string, type: 'success'|'info'|'warning'|'error'} | null>(null);

  // --- HANDLERS ---
  const triggerToast = (message: string, type: 'success'|'info'|'warning'|'error' = 'info') => {
    setToast({ message, type });
    setTimeout(() => setToast(null), 3000);
  };

  const toggleOfflineMode = () => {
    if (!isOffline) {
      setIsOffline(true);
      setSyncQueue(3);
      triggerToast('Offline mode activated. Essential records remain available.', 'warning');
    } else {
      setIsOffline(false);
    }
  };

  const handleSync = () => {
    if (syncQueue === 0) return;
    setIsSyncing(true);
    setTimeout(() => {
      setSyncQueue(0);
      setIsSyncing(false);
      triggerToast('Sync completed successfully.', 'success');
    }, 1500);
  };

  const startJudgeDemo = () => {
    setDemoMode(true);
    setCurrentView('patient_profile');
    setIsOffline(false);
    setSyncQueue(0);
    setReferralStep(0);
    triggerToast('Judge Demo Mode Initialized: Scenario Loaded.', 'info');
  };

  const advanceReferral = () => {
    if (referralStep < REFERRAL_STAGES.length - 1) {
      setReferralStep(prev => prev + 1);
      if (referralStep === 3) {
        triggerToast('Outcome recorded successfully. Care continuity maintained.', 'success');
      }
    }
  };

  // --- COMPONENTS ---
  const Sidebar = () => (
    <div className="w-64 bg-slate-900 text-slate-300 flex flex-col h-screen fixed left-0 top-0">
      <div className="p-6 flex items-center gap-3 text-white font-bold text-xl border-b border-slate-800">
        <Activity className="text-teal-400" /> MEDIREACH
      </div>
      <nav className="flex-1 p-4 space-y-2">
        {[
          { id: 'dashboard', icon: Activity, label: 'Dashboard' },
          { id: 'patients', icon: Users, label: 'Patients' },
          { id: 'referrals', icon: FileText, label: 'Referrals' },
          { id: 'teleconsultation', icon: Video, label: 'Teleconsultation' },
        ].map((item) => (
          <button
            key={item.id}
            onClick={() => setCurrentView(item.id)}
            className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl transition-all ${
              currentView === item.id || (currentView === 'patient_profile' && item.id === 'patients')
                ? 'bg-teal-500/10 text-teal-400 font-medium'
                : 'hover:bg-slate-800 hover:text-white'
            }`}
          >
            <item.icon size={20} />
            {item.label}
          </button>
        ))}
      </nav>
      <div className="p-4 border-t border-slate-800">
        <button 
          onClick={startJudgeDemo}
          className="w-full flex items-center justify-center gap-2 bg-indigo-600/20 text-indigo-400 px-4 py-3 rounded-xl hover:bg-indigo-600/30 transition-colors font-medium border border-indigo-500/30"
        >
          <Play size={16} /> Judge Demo Mode
        </button>
      </div>
    </div>
  );

  const Topbar = () => (
    <div className="h-16 bg-white border-b border-slate-200 flex items-center justify-between px-6 sticky top-0 z-20 ml-64">
      <div className="flex items-center gap-4 w-96">
        <div className="relative w-full">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" size={18} />
          <input 
            type="text" 
            placeholder="Search patients, IDs..." 
            className="w-full pl-10 pr-4 py-2 bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-teal-500/50 text-sm"
          />
        </div>
      </div>
      <div className="flex items-center gap-6">
        {/* Connectivity Component */}
        <div className="flex items-center gap-3 bg-slate-50 px-3 py-1.5 rounded-lg border border-slate-200">
          <button onClick={toggleOfflineMode} className="flex items-center gap-2 text-sm font-medium">
            {isOffline ? (
              <><WifiOff size={16} className="text-amber-500" /> <span className="text-amber-700">Offline Mode</span></>
            ) : (
              <><Wifi size={16} className="text-teal-500" /> <span className="text-teal-700">Online</span></>
            )}
          </button>
          {isOffline && syncQueue > 0 && (
            <button 
              onClick={handleSync}
              className={`flex items-center gap-1.5 text-xs font-semibold px-2 py-1 rounded bg-amber-100 text-amber-800 hover:bg-amber-200 transition-colors ${isSyncing ? 'animate-pulse' : ''}`}
            >
              <RefreshCw size={12} className={isSyncing ? 'animate-spin' : ''} />
              {isSyncing ? 'Syncing...' : `${syncQueue} Queued`}
            </button>
          )}
        </div>
        
        <div className="flex items-center gap-4 text-slate-500">
          <Globe size={20} className="hover:text-slate-800 cursor-pointer" />
          <Bell size={20} className="hover:text-slate-800 cursor-pointer" />
          <div className="w-8 h-8 bg-teal-100 text-teal-700 rounded-full flex items-center justify-center font-bold border border-teal-200">
            HW
          </div>
        </div>
      </div>
    </div>
  );

  const LandingPage = () => (
    <div className="min-h-screen bg-slate-50 flex flex-col relative overflow-hidden">
      <div className="absolute top-0 inset-x-0 h-96 bg-gradient-to-b from-blue-900 to-slate-50 opacity-90"></div>
      <div className="relative z-10 flex-1 flex flex-col items-center justify-center text-center px-4">
        <div className="inline-flex items-center gap-2 bg-teal-500/10 text-teal-700 px-4 py-2 rounded-full font-medium text-sm mb-8 border border-teal-500/20">
          <Activity size={16} /> SIH26133 • Synthetic Demo Data
        </div>
        <h1 className="text-6xl font-extrabold text-slate-900 tracking-tight mb-6">
          MEDIREACH
        </h1>
        <p className="text-2xl text-slate-700 mb-4 font-medium max-w-2xl">
          Healthcare continuity, even beyond connectivity.
        </p>
        <p className="text-slate-500 max-w-3xl mb-12 text-lg">
          A unified digital platform connecting frontline health workers, healthcare facilities, and patients across rural and underserved communities.
        </p>
        <div className="flex items-center gap-4">
          <button 
            onClick={() => setCurrentView('dashboard')}
            className="bg-blue-900 text-white px-8 py-4 rounded-xl font-semibold hover:bg-blue-800 transition-all shadow-lg hover:shadow-xl flex items-center gap-2"
          >
            Open Demo Dashboard <ArrowRight size={20} />
          </button>
          <button 
            onClick={startJudgeDemo}
            className="bg-white text-blue-900 border border-slate-200 px-8 py-4 rounded-xl font-semibold hover:bg-slate-50 transition-all flex items-center gap-2"
          >
            <Play size={20} className="text-teal-600" /> Judge Demo Mode
          </button>
        </div>

        <div className="mt-20 flex items-center gap-8 text-sm font-medium text-slate-500">
          <div className="flex flex-col items-center gap-2"><div className="w-12 h-12 rounded-full bg-white shadow-sm flex items-center justify-center"><Users className="text-blue-600"/></div>Community</div>
          <ArrowRight className="text-slate-300"/>
          <div className="flex flex-col items-center gap-2"><div className="w-12 h-12 rounded-full bg-white shadow-sm flex items-center justify-center"><Stethoscope className="text-teal-600"/></div>Frontline Worker</div>
          <ArrowRight className="text-slate-300"/>
          <div className="flex flex-col items-center gap-2"><div className="w-12 h-12 rounded-full bg-white shadow-sm flex items-center justify-center"><Activity className="text-indigo-600"/></div>PHC / Hospital</div>
        </div>
      </div>
    </div>
  );

  const Dashboard = () => (
    <div className="p-8 max-w-7xl mx-auto space-y-8 animate-in fade-in duration-500">
      <div className="flex justify-between items-end">
        <div>
          <h2 className="text-2xl font-bold text-slate-900">Good morning, Health Worker</h2>
          <p className="text-slate-500 mt-1">Here’s today's healthcare continuity overview.</p>
        </div>
        <div className="text-xs text-slate-400 bg-slate-100 px-3 py-1 rounded-md">Prototype • Synthetic Demo Data</div>
      </div>

      <div className="grid grid-cols-4 gap-6">
        {[
          { label: 'Active Patients', value: '128', icon: Users, color: 'text-blue-600', bg: 'bg-blue-50' },
          { label: 'Open Referrals', value: '07', icon: FileText, color: 'text-indigo-600', bg: 'bg-indigo-50' },
          { label: 'Follow-ups Due', value: '11', icon: AlertCircle, color: 'text-amber-600', bg: 'bg-amber-50' },
          { label: 'Pending Sync', value: isOffline ? syncQueue : '0', icon: RefreshCw, color: 'text-slate-600', bg: 'bg-slate-50' },
        ].map((kpi, i) => (
          <div key={i} className="bg-white p-6 rounded-2xl border border-slate-100 shadow-sm hover:shadow-md transition-shadow">
            <div className={`w-12 h-12 ${kpi.bg} ${kpi.color} rounded-xl flex items-center justify-center mb-4`}>
              <kpi.icon size={24} />
            </div>
            <div className="text-3xl font-bold text-slate-900">{kpi.value}</div>
            <div className="text-sm font-medium text-slate-500 mt-1">{kpi.label}</div>
          </div>
        ))}
      </div>

      <div className="grid grid-cols-3 gap-6">
        <div className="col-span-2 bg-white p-6 rounded-2xl border border-slate-100 shadow-sm">
          <h3 className="text-lg font-bold text-slate-900 mb-6">Care Continuity Trends</h3>
          <div className="h-64">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={analyticsData}>
                <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#e2e8f0" />
                <XAxis dataKey="name" axisLine={false} tickLine={false} tick={{fill: '#64748b'}} />
                <YAxis axisLine={false} tickLine={false} tick={{fill: '#64748b'}} />
                <Tooltip contentStyle={{borderRadius: '8px', border: 'none', boxShadow: '0 4px 6px -1px rgb(0 0 0 / 0.1)'}} />
                <Line type="monotone" dataKey="referrals" stroke="#0f172a" strokeWidth={3} dot={{r: 4, strokeWidth: 2}} />
                <Line type="monotone" dataKey="followUps" stroke="#14b8a6" strokeWidth={3} dot={{r: 4, strokeWidth: 2}} />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </div>

        <div className="bg-white p-6 rounded-2xl border border-slate-100 shadow-sm flex flex-col">
          <h3 className="text-lg font-bold text-slate-900 mb-4">Priority Actions</h3>
          <div className="space-y-4 flex-1">
            <div className="p-4 rounded-xl border border-amber-200 bg-amber-50">
              <div className="flex items-center gap-2 text-amber-800 font-bold text-sm mb-2">
                <AlertCircle size={16} /> URGENT FOLLOW-UP
              </div>
              <p className="text-sm text-slate-700 font-medium">Patient: MR-1042 (Anita Devi)</p>
              <p className="text-xs text-slate-500 mt-1">Reason: Maternal follow-up</p>
              <p className="text-xs text-slate-500 mb-3">Status: Appointment pending</p>
              <button 
                onClick={() => setCurrentView('patient_profile')}
                className="w-full bg-amber-600 text-white text-sm font-semibold py-2 rounded-lg hover:bg-amber-700 transition-colors"
              >
                View Case
              </button>
            </div>
            
            <div className="p-4 rounded-xl border border-slate-200 bg-slate-50">
              <div className="flex items-center gap-2 text-slate-700 font-bold text-sm mb-2">
                <Activity size={16} /> REFERRAL NEEDS ATTENTION
              </div>
              <p className="text-sm text-slate-700 font-medium">Patient: MR-1037</p>
              <p className="text-xs text-slate-500 mt-1">Status: Awaiting hospital response</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );

  const PatientProfile = () => (
    <div className="p-8 max-w-6xl mx-auto space-y-6 animate-in slide-in-from-right-4 duration-300">
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-4">
          <button onClick={() => setCurrentView('dashboard')} className="p-2 hover:bg-slate-100 rounded-full transition-colors text-slate-500">
            <ChevronRight className="rotate-180" />
          </button>
          <div>
            <h2 className="text-2xl font-bold text-slate-900">Anita Devi</h2>
            <p className="text-slate-500">ID: MR-1042 • Female, 28 yrs • Village: Palghar</p>
          </div>
        </div>
        <div className="flex items-center gap-3">
          <span className="px-3 py-1 bg-amber-100 text-amber-800 rounded-full text-xs font-bold border border-amber-200">High Risk</span>
          <span className="text-xs text-slate-400 bg-slate-100 px-3 py-1 rounded-md">Synthetic Demo Data</span>
        </div>
      </div>

      <div className="grid grid-cols-3 gap-6">
        <div className="col-span-2 space-y-6">
          <div className="bg-white p-6 rounded-2xl border border-slate-100 shadow-sm">
            <h3 className="text-lg font-bold text-slate-900 mb-4 flex items-center justify-between">
              Smart Referral Journey
              <span className="text-sm font-normal text-teal-600 bg-teal-50 px-3 py-1 rounded-full">Active</span>
            </h3>
            
            <div className="relative pt-8 pb-4">
              <div className="absolute top-10 left-6 right-6 h-1 bg-slate-100 rounded-full"></div>
              <div 
                className="absolute top-10 left-6 h-1 bg-teal-500 rounded-full transition-all duration-500" 
                style={{ width: `${(referralStep / (REFERRAL_STAGES.length - 1)) * 100}%` }}
              ></div>
              
              <div className="relative flex justify-between">
                {REFERRAL_STAGES.map((stage, index) => {
                  const isActive = index <= referralStep;
                  const isCurrent = index === referralStep;
                  return (
                    <div key={stage} className="flex flex-col items-center w-24">
                      <div className={`w-6 h-6 rounded-full border-2 flex items-center justify-center bg-white z-10 transition-colors ${
                        isActive ? 'border-teal-500' : 'border-slate-300'
                      }`}>
                        {isActive && <div className="w-2.5 h-2.5 bg-teal-500 rounded-full" />}
                      </div>
                      <span className={`text-xs mt-3 text-center font-medium ${isCurrent ? 'text-teal-700' : isActive ? 'text-slate-700' : 'text-slate-400'}`}>
                        {stage}
                      </span>
                    </div>
                  );
                })}
              </div>
            </div>

            <div className="mt-8 p-4 bg-slate-50 rounded-xl border border-slate-200 flex items-center justify-between">
              <div>
                <p className="text-sm text-slate-500 mb-1">Current Status</p>
                <p className="font-semibold text-slate-900">{REFERRAL_STAGES[referralStep]}</p>
                <p className="text-xs text-slate-500 mt-1">Sub-Centre → District Hospital (Maternal follow-up)</p>
              </div>
              
              {referralStep < REFERRAL_STAGES.length - 1 ? (
                <button 
                  onClick={advanceReferral}
                  className="bg-blue-900 text-white px-6 py-2 rounded-lg text-sm font-semibold hover:bg-blue-800 transition-colors shadow-sm"
                >
                  {referralStep === 3 ? 'Mark Outcome Received' : 'Simulate Next Step'}
                </button>
              ) : (
                <div className="flex items-center gap-2 text-teal-600 font-bold text-sm bg-teal-50 px-4 py-2 rounded-lg border border-teal-200">
                  <CheckCircle size={16} /> Referral Closed
                </div>
              )}
            </div>
          </div>

          <div className="bg-white p-6 rounded-2xl border border-slate-100 shadow-sm">
            <h3 className="text-lg font-bold text-slate-900 mb-4">Care History</h3>
            <div className="space-y-6 pl-4 border-l-2 border-slate-100">
              {[
                { date: 'Today, 10:42 AM', title: 'Specialist Consultation', desc: 'Conducted via teleconsultation at PHC.' },
                { date: 'Yesterday, 09:15 AM', title: 'Referral Created', desc: 'Referred to District Hospital due to elevated BP.' },
                { date: 'Oct 12, 2026', title: 'Routine ANC Visit', desc: 'Vitals recorded. Iron supplements provided.' }
              ].map((event, i) => (
                <div key={i} className="relative">
                  <div className="absolute -left-[21px] top-1 w-3 h-3 bg-white border-2 border-slate-300 rounded-full"></div>
                  <p className="text-xs text-slate-400 font-medium mb-1">{event.date}</p>
                  <p className="text-sm font-bold text-slate-800">{event.title}</p>
                  <p className="text-sm text-slate-600 mt-1">{event.desc}</p>
                </div>
              ))}
            </div>
          </div>
        </div>

        <div className="space-y-6">
          <div className="bg-indigo-50 border border-indigo-100 p-6 rounded-2xl relative overflow-hidden">
            <div className="absolute top-0 right-0 p-3 opacity-10">
              <Activity size={64} />
            </div>
            <h3 className="text-sm font-bold text-indigo-900 mb-2 flex items-center gap-2">
              ✨ AI Care Assistant
            </h3>
            <p className="text-xs text-indigo-700 bg-white/60 inline-block px-2 py-1 rounded mb-4">
              AI-assisted recommendation • For decision support only
            </p>
            <div className="text-sm text-indigo-900 space-y-3 relative z-10">
              <p><strong>Observation:</strong> Elevated blood pressure trend across last 2 ANC visits.</p>
              <p><strong>Suggested Action:</strong> Prioritize specialist follow-up. Ensure referral outcome is recorded in the system.</p>
              <button className="w-full bg-indigo-600 text-white py-2 rounded-lg text-sm font-semibold shadow-sm hover:bg-indigo-700 mt-2">
                Generate Follow-up Reminder
              </button>
            </div>
          </div>

          <div className="bg-white p-6 rounded-2xl border border-slate-100 shadow-sm">
            <h3 className="text-sm font-bold text-slate-900 mb-4">Patient Demographics</h3>
            <div className="space-y-3 text-sm">
              <div className="flex justify-between border-b border-slate-50 pb-2">
                <span className="text-slate-500">Contact</span>
                <span className="font-medium text-slate-900">+91 98765 43210</span>
              </div>
              <div className="flex justify-between border-b border-slate-50 pb-2">
                <span className="text-slate-500">Village</span>
                <span className="font-medium text-slate-900">Palghar, Ward 4</span>
              </div>
              <div className="flex justify-between border-b border-slate-50 pb-2">
                <span className="text-slate-500">Assigned ASHA</span>
                <span className="font-medium text-slate-900">Sunita M.</span>
              </div>
              <div className="flex justify-between">
                <span className="text-slate-500">Nearest PHC</span>
                <span className="font-medium text-slate-900">Palghar PHC (8km)</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );

  return (
    <div className="flex h-screen bg-slate-50 font-sans overflow-hidden">
      {/* Toast Notification */}
      {toast && (
        <div className={`fixed bottom-6 right-6 z-50 px-6 py-4 rounded-xl shadow-xl flex items-center gap-3 border animate-in slide-in-from-bottom-4 ${
          toast.type === 'success' ? 'bg-teal-50 border-teal-200 text-teal-900' :
          toast.type === 'warning' ? 'bg-amber-50 border-amber-200 text-amber-900' :
          'bg-white border-slate-200 text-slate-900'
        }`}>
          {toast.type === 'success' ? <CheckCircle className="text-teal-500" /> : <AlertCircle className={toast.type === 'warning' ? 'text-amber-500' : 'text-slate-500'} />}
          <span className="font-medium text-sm">{toast.message}</span>
        </div>
      )}

      {currentView === 'landing' ? (
        <LandingPage />
      ) : (
        <>
          <Sidebar />
          <div className="flex-1 flex flex-col h-screen ml-64 overflow-y-auto">
            <Topbar />
            
            {demoMode && (
              <div className="bg-indigo-600 text-white px-6 py-3 flex items-center justify-between shadow-md">
                <div className="flex items-center gap-3">
                  <Play size={18} className="fill-white" />
                  <span className="font-bold">Judge Demo Flow Active</span>
                  <span className="text-indigo-200 text-sm ml-2">Scenario: Rural patient requiring specialist follow-up.</span>
                </div>
                <button 
                  onClick={() => setDemoMode(false)}
                  className="text-xs bg-indigo-800 px-3 py-1.5 rounded-lg font-medium hover:bg-indigo-900 transition-colors"
                >
                  Exit Demo
                </button>
              </div>
            )}

            <main className="flex-1 bg-slate-50/50">
              {currentView === 'dashboard' && <Dashboard />}
              {currentView === 'patient_profile' && <PatientProfile />}
              {/* Other views would be implemented similarly, routing based on currentView */}
              {(currentView === 'patients' || currentView === 'referrals' || currentView === 'teleconsultation') && (
                <div className="p-8 flex flex-col items-center justify-center h-full text-slate-400">
                  <Activity size={48} className="mb-4 opacity-20" />
                  <p className="text-lg font-medium">Module Selected: {currentView}</p>
                  <p className="text-sm mt-2">Use the Dashboard or Judge Demo Mode for the primary SIH evaluation flow.</p>
                </div>
              )}
            </main>
          </div>
        </>
      )}
    </div>
  );
}