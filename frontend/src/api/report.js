import axios from 'axios';
import { useQuery,
  // useMutation
} from '@tanstack/react-query';
//import queryClient from '@services/queryClient';
// import { toast } from 'react-toastify';

export const useReport = (params) => {
  return useQuery({
    queryKey: ['report'],
    queryFn: () => axios.get(`/report/`, { params: params }).then((res) => res.data)});
};
