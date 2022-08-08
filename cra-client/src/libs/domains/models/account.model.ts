export interface IAccountModel {
  id: string;
  name: string;
  number: string;
  currency: string;
  balance: number;
  branch?: string;
}
