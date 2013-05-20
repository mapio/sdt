mbeans_configuration = [
	[{
		name: 'java.lang:type=Memory',
		attribute: 'HeapMemoryUsage',
		path: 'committed'
	},{
		name: 'java.lang:type=Memory',
		attribute: 'HeapMemoryUsage',
		path: 'used'
	}],
	[{
		name: 'java.lang:type=OperatingSystem',
		attribute: 'SystemLoadAverage'
	}],
	[{
		name:     'java.lang:type=Threading',
		attribute: 'ThreadCount'
	}],
	[{
		name:     'java.lang:type=Threading',
		attribute: 'CurrentThreadCpuTime'
	}]
];
